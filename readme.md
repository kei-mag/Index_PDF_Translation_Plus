# Indqx PDF 翻訳 Plus

本リポジトリは、Mega-Gorilla様の[Index_PDF_Translation](https://github.com/Mega-Gorilla/Index_PDF_Translation)のフォークです。
以下の翻訳サービスのサポートと、GUIを追加します。
- [llama.cpp](https://github.com/ggerganov/llama.cpp)によるローカルLLM翻訳（ユーザーのPC上で動く生成AIモデルで翻訳を行います）
- コピペ翻訳（APIを使わずに翻訳するために、ユーザーに翻訳サイト上で訳文のコピペを求めます）
-  Google翻訳
-  Microsoft Translator

開発はfletを使用し、ローカルアプリまたはWebアプリとしてホスティングして使用できるようにする予定です。

> [!NOTE]
> 開発中　完了未定

## 計画
*️⃣：未着手，➡️：進行中，✅：完了

➡️ ディレクトリ構成の変更  
➡️ GUIの追加  
*️⃣ LLM翻訳のサポート  
*️⃣ llama.cpp構築のためのDocker Composeファイルの追加  
*️⃣ コピペ翻訳のサポート  
*️⃣ Google翻訳のサポート  
*️⃣ Microsoft Translatorのサポート  
*️⃣ マルチユーザー対応  

<!-- ## 使い方
-----
1. docker-composeでサービスを起動します。
   ```sh
   docker-compose up -d
   ```
   CUDAを利用できる環境の方はこちらで起動してください
   ```
   USE=CUDA docker-compose up -d
   ```
   OpenBLASを利用できる環境の方（Intel Xe Graphics, Arc GPU）はこちらで起動してください
   ```
   USE=OBLAS docker-compose up -d
   ```
2. ブラウザで`localhost`にアクセスします
3.  -->