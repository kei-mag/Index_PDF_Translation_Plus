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

## 使い方

* [OpenBLAS](#openblas)
* [CUDA（nvidia製のGPUを搭載したPCの場合）](#cuda)
* [ROCm（amd製のGPUを搭載したPCの場合）](#rocm)
* [SYCL（intel製のGPUを搭載したPCの場合）](#sycl)
* [Vulkan](#vulkan)
* [CPUのみ](#cpuのみ)

---

### 前提

* Docker（および Docker Compose V2）がインストールされていること
* GPU バックエンドを使う場合は、

  * NVIDIA: [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker) がセットアップ済みで `nvidia-smi` が動作すること
  * AMD ROCm: ROCm ドライバがインストールされ `rocm-smi` が動作すること

---

### バックエンド別起動コマンド

#### OpenBLAS

```bash
# リポジトリをクローンして初回ビルド
git clone <リポジトリURL>
cd <リポジトリ名>
# デフォルトの OpenBLAS バックエンドで起動
docker compose up --build
```

#### CUDAnvidia製のGPUを搭載したPCの場合）

```bash
# GPU が認識されているか確認	nvidia-smi
# CUDA バックエンドで起動 (ワンライナー)
LLAMA_CPP_BACKEND=cuda docker compose up --build --gpus all
```

#### ROCmamd製のGPUを搭載したPCの場合）

```bash
# ROCm が認識されているか確認	rocm-smi
# ROCm バックエンドで起動 (ワンライナー)
LLAMA_CPP_BACKEND=rocm docker compose up --build \
  --device /dev/kfd:/dev/kfd \
  --device /dev/dri:/dev/dri
```

#### SYCLintel製のGPUを搭載したPCの場合）

```bash
# SYCL バックエンドで起動 (ワンライナー)
LLAMA_CPP_BACKEND=sycl docker compose up --build
```

#### Vulkan

```bash
# Vulkan バックエンドで起動 (ワンライナー)
LLAMA_CPP_BACKEND=vulkan docker compose up --build
```

#### CPUのみ

```bash
# 純粋に CPU 演算のみで起動 (ワンライナー)
LLAMA_CPP_BACKEND=cpu docker compose up --build
```

---

## 2回目以降の起動

一度ビルドが成功していれば、`--build` オプションなしで起動できます：

```bash
docker compose up
```

---

## バックエンドを途中で切り替える場合

1. 環境変数 `LLAMA_CPP_BACKEND` を任意の値に指定して再起動

   ```bash
   # 例：OpenBLAS に戻す
   LLAMA_CPP_BACKEND=openblas docker compose up --build
   ```

2. 必要に応じて GPU オプションを追加

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).