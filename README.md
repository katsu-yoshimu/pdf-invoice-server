# pdf-invoice-server

Vercel 上で動作する PDF 請求書を AI で読込み情報抽出するための WebAPI です。[環境構築](#環境構築)を参照して、Vercel の本番環境構築してください。

なお、今後の改修やデバックを行うための開発環境として、ローカルPCで動作させたい場合は[ローカル環境実行](#ローカル環境実行)を参照ください。

## 目次

- [環境構築](#環境構築) ※本番環境、これだけで実運用可能です。
- [ローカル環境構築](#ローカル環境構築) ※開発環境
- [ローカル環境実行](#ローカル環境実行) ※開発環境
- [ライセンス](#ライセンス)
- [参考リンク](#参考リンク)

## 環境構築

前提：**Gemini APIキー**取得済。**GitHub**アカウント登録済

- Gemini APIキーの取得方法は[参考リンク](#参考リンク)を参照ください。
- GitHub アカウントの登録方法は[参考リンク](#参考リンク)を参照ください。

1. **Vercel & Github 追加:**

   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2Fpdf-invoice-server)

   上のボタンを押すと Vercel ページに遷移します。その後、Vercel & Github を追加します。

   手順は以下のとおりです。
   - 「Continue with GitHub」ボタンをクリック
   - GitHub ユーザ名、パスワードを入力し「Sign in」ボタンをクリック
   - 「Private Repository Name」に「pdf-invoice-server」を入力し「Create」ボタンをクリック
   - しばらく待っている(30秒ぶらい)と「Congratulations!」が表示される。「Continue to Dashboard」ボタンをクリック
   - 「Domains」記載されたドメインをクリックすると別ウインドウでTOP画面を表示
   - URLに「/docs」を追加して「Enter」キーを入力するとWebAPIが実行できる画面を表示 ← ※注意※ 以下の Gemini APIキー設定 をするまでは実行（「Execute」ボタンをクリック）してもエラーとなります。

2. **Gemini APIキー設定:**

   手順は以下のとおりです。
    - 「Dashboard」を表示 ← 上記の 「Continue to Dashboard」ボタンをクリック にて表示された画面
    - 上メニュー「Settings」をクリック
    - 左メニュー「Environment Variables」をクリック
    - 「key」に「GEMINI_API_KEY」、「Value」に {Geimini APIキー値} を入力し、「Save」ボタンをクリック
    - 「Redeply」ボタンをクリック
    - 「Redeply」ボタンをクリック ← この実行にて有効となる

3. **ブラウザで以下のURLでアクセス:**

   [https://pdf-invoice-server.vercel.app/docs](https://pdf-invoice-server.vercel.app/docs)

   注意：「pdf-invoice-server」は 1. の結果で書き替えてください。

4. **このページからWebAPIの実行できる**

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
   set GEMINI_API_KEY={Geimini APIキー値で置換してください} 
   python api/exctract_invoice.py
   ```

2. **ブラウザで以下のURLでアクセス:**

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. **このページからWebAPIの実行できる**

## ライセンス

ライセンスは Apache2 License に準拠します。

## 参考リンク

1. [Qiita 【完全無料】Gemini APIチュートリアル（所要時間10分） - APIキーの取得](https://qiita.com/zukki2/items/10bfeb1c4330aa18ff87#step1api%E3%82%AD%E3%83%BC%E3%81%AE%E5%8F%96%E5%BE%97)

   Gemini APIキーの取得方法はここを参考にしてください。

2. [GitHub でのアカウントの作成](https://docs.github.com/ja/get-started/start-your-journey/creating-an-account-on-github)

   GitHub のアカウント作成方法ここを参考にしてください。

   以下も参考にしてください。
   - メールアドレスが必要です。「lunch Code」がメール通知されます。
   - 「How would you describe youself?」は「N/A」を選択してください。必要に応じて変更してください。
   - 「How many team members will be working with you?」は「Just me」を選択してください。必要に応じて変更してください。
   - 「What are the top 2 things you want to do with GitHub?」は適当に2つを選択してください。
