# Local Index_PDF_Translation

本リポジトリは、Mega-Gorilla様の[Index_PDF_Translation](https://github.com/Mega-Gorilla/Index_PDF_Translation)のフォークです。
以下の翻訳サービスのサポートと、GUIを追加します。
- Google翻訳（Google App Script Translate API）
- コピペ翻訳（APIを使わずに翻訳するために、ユーザーに翻訳サイト上で訳文のコピペを求めます）
- [llama.cpp](https://github.com/ggerganov/llama.cpp)によるローカルLLM翻訳（ユーザーのPC上で動く生成AIモデルで翻訳を行います）

## 使い方
> [!NOTE]
> 開発中　完了未定
以下予定している使い方
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
3. 