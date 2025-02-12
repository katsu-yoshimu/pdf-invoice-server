# pdf-invoice-server（作成中）

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2Fpdf-invoice-server)

Vercel 上で動作する PDF 請求書を AI で読込み情報抽出するための WebAPI です。[環境構築](#環境構築)を参照して、Vercel環境構築してください。
なお、ローカルPCでも動作させたい場合は[ローカル環境実行](#ローカル環境実行)を参照ください。

## 目次

- [環境構築](#環境構築)
- [ローカル環境構築](#ローカル環境構築)
- [ローカル環境実行](#ローカル環境実行)
- [ライセンス](#ライセンス)

## 環境構築

前提：**Gemini APIキー**取得済。**Vercel**アカウント登録済。
　　　- Gemini APIキーの取得方法は参考リンクを参照ください。
　　　- Vercelアカウントの登録方法は・・・・を参照ください。

1. **Vercel & Github 新規追加:**

   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2Fpdf-invoice-server)

   上のボタンを押すと Vercel ページに遷移します。その後、Vercel & Github を追加します。

2. **GeminiAPIキー設定:**

    - 上メニュー「Settings」をクリック
    - 左メニュー「Environment Variables」をクリック
    - 「key」に「GEMINI_API_KEY」を入力
    - 「Value」に{Geimini APIキー値}を入力
    - 「Save」ボタンをクリック
    - 「Redeply」を実行にて有効となる

3. **ブラウザで以下のURLでアクセス:**

   [https://pdf-invoice-server.vercel.app/docs](https://pdf-invoice-server.vercel.app/docs)

   注意：「pdf-invoice-server」は1.の結果で書き替えてください。

4. このページからWebAPIの実行できる

## ローカル環境構築

前提：ローカルPCに **git、ptyhon3.12** がインストール済＆**Gemini APIキー**取得済

1. **ローカルPCにリポジトリのクーロン作成:**

   ```cmd
   git clone https://github.com/katsu-yoshimu/pdf-invoice-server.git
   ```

2. **ローカルPCに仮想完了作成と仮想環境アクティベート:**

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **ローカルPCに必要なPythonパッケージをインストール:**

   ```cmd
   cd pdf-invoice-server
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## ローカル環境実行

1. **WebAPIサーバ起動:**

   ```cmd
   cd pdf-invoice-server
   .venv\Scripts\activate
   set GEMINI_API_KEY=（ここは取得したAPIキー値で置き換えてください） 
   python api/exctract_invoice.py
   ```

2. **ブラウザで以下のURLでアクセス:**

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. このページからWebAPIの実行できる

## ライセンス

ライセンスは Apache2 License に準拠します。

## 参考

- [Qiita 【完全無料】Gemini APIチュートリアル（所要時間10分） - APIキーの取得](https://qiita.com/zukki2/items/10bfeb1c4330aa18ff87#step1api%E3%82%AD%E3%83%BC%E3%81%AE%E5%8F%96%E5%BE%97)

    Gemini APIキーの取得方法はここを参考にしてください。
