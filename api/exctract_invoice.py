from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional
import logging
import filetype
import google.generativeai as genai
import os
import base64
import re
import json

app = FastAPI()

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Gemini APIの設定
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

def validate_file(file_content: bytes) -> str:
    """ファイルの種類を検証し、MIMEタイプを返す"""
    file_type = filetype.guess(file_content)
    if file_type.mime != 'application/pdf':
        raise HTTPException(status_code=400, detail="PDFファイルを指定してください")
    return file_type.mime

def build_prompt(notes: Optional[str]) -> str:
    """プロンプトを構築する"""
    prompt = """この請求書PDFから項目を抽出して回答してください。

# 抽出項目
1. 日付（形式は、2024年10月11日 → 20241011 とする）
2. 請求元名
3. 請求金額（形式は、単位、カンマを除き数値のみとする）

# 回答形式
- JSON形式で回答する
- キー値は「日付」は「date」、「請求元名」は「issuer」、「請求金額」は「amount」とする
- JSON形式の回答が配列になる場合は配列の先頭を回答して配列にしない
"""

    if notes:
        prompt += "\n\n# 注意事項:\n" + notes

    return prompt

def extract_code_block(response_text):
    """Geminiのレスポンスからコードブロックを抽出する"""
    # コードブロックの正規表現パターン
    pattern = r'```(?:[^\n]*\n)?([\s\S]*?)(?:```|$)'
    
    # 最初のコードブロックを検索
    match = re.search(pattern, response_text)
    
    if match:
        # コードブロックの内容を返す
        return match.group(1).strip()
    else:
        # コードブロックが見つからない場合はNoneを返す
        return None

@app.post("/api/exctract_invoice/")
async def exctract_invoice(
    file: UploadFile = File(...),
    notes: Optional[str] = Form(None)
):
    try:
        # ファイルの内容を読み取る
        file_content = await file.read()
        file_size = len(file_content)
        await file.close()

        # ファイルの種類を検証
        file_type = validate_file(file_content)

        # ファイルをBase64エンコード
        doc_data = base64.standard_b64encode(file_content).decode("utf-8")

        # プロンプトを構築
        prompt = build_prompt(notes)

        # Gemini API 呼び出し
        gemini_response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])

        # 請求書データを抽出
        # レスポンスのJSON形式のコードブロックを抽出
        # JSON形式のコードブロックに日付、請求元、金額が設定されている
        invoice_data = json.loads(extract_code_block(gemini_response.text))

        # レスポンス用のデータを作成
        response_data = {
            "invoice_data": invoice_data,
            "filename": file.filename,                    # 参考情報
            "file_size": file_size,                       # 参考情報
            "file_type": file_type,                       # 参考情報
            "notes": notes,                               # 参考情報
            "gemini_prompt" : prompt,                     # 参考情報
            "gemini_response": gemini_response.to_dict()  # 参考情報
        }

        logger.info(f"File uploaded: {file.filename}, Size: {file_size} bytes, file_type: {file_type}, notes: {notes}")
        return JSONResponse(content=response_data, status_code=200)

    except HTTPException as he:
        logger.error(f"HTTPException: {he.detail}")
        raise he
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def index():
    html = """<html>
    <head>
        <meta charset="utf-8"/>
        <title>pdf-inoice-server</title>
    </head>
    <body>
        <h1>pdf-inoice-server</h1>
        PDF請求書をAIで読込み情報抽出するAPIです。<br/>
        使用方法は以下をご確認ください。
        <li>
            <a href="/docs">Swagger - API仕様</a>
        </li>
    </body>
</html>"""
    return HTMLResponse(content=html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("exctract_invoice:app", host="0.0.0.0", port=8000)
