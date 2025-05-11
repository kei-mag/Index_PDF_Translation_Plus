# 1) デフォルトバックエンドを openblas に設定
ARG LLAMA_CPP_BACKEND=openblas
FROM python:3.12-slim

WORKDIR /app

# 2) 共通ツール類のみ先にインストール
RUN apt-get update && \
    apt-get install -y \
      build-essential cmake git wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 3) バックエンド別の最小限パッケージをインストール
ARG LLAMA_CPP_BACKEND
RUN set -eux; \
    case "$LLAMA_CPP_BACKEND" in \
      openblas) \
        apt-get update && \
        apt-get install -y pkg-config libopenblas-dev && \
        rm -rf /var/lib/apt/lists/* \
        ;; \
      vulkan) \
        apt-get update && \
        apt-get install -y libvulkan-dev vulkan-tools glslang-tools && \
        rm -rf /var/lib/apt/lists/* \
        ;; \
      cuda) \
        apt-get update && \
        wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb && \
        dpkg -i cuda-keyring_1.1-1_all.deb && \
        apt-get update && \
        apt-get install -y cuda-toolkit && \
        rm -rf cuda-keyring_1.1-1_all.deb /var/lib/apt/lists/* \
        ;; \
      rocm) \
        apt-get update && \
        wget -qO - https://repo.radeon.com/rocm/rocm-keyring.gpg | apt-key add - && \
        echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ bookworm main' \
          > /etc/apt/sources.list.d/rocm.list && \
        apt-get update && \
        apt-get install -y rocm-dev && \
        rm -rf /var/lib/apt/lists/* \
        ;; \
      sycl) \
        apt-get update && \
        wget -qO- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \
          | apt-key add - && \
        echo "deb https://apt.repos.intel.com/oneapi all main" \
          > /etc/apt/sources.list.d/intel-oneapi.list && \
        apt-get update && \
        apt-get install -y \
          intel-oneapi-basekit \
          intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic && \
        rm -rf /var/lib/apt/lists/* \
        ;; \
      cpu) \
        # CPUのみ: 追加パッケージ不要 \
        ;; \
      *) \
        echo "Unknown LLAMA_CPP_BACKEND: $LLAMA_CPP_BACKEND" >&2; \
        exit 1 \
        ;; \
    esac

# 4) Python依存＋llama-cpp-python のビルド
COPY requirements.txt .
RUN set -eux; \
    # バックエンドごとの CMAKE_ARGS
    case "$LLAMA_CPP_BACKEND" in \
      cuda)     CMAKE_ARGS="-DGGML_CUDA=on" ;; \
      rocm)     CMAKE_ARGS="-DGGML_HIPBLAS=on" ;; \
      openblas) CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" ;; \
      vulkan)   CMAKE_ARGS="-DGGML_VULKAN=on" ;; \
      sycl)     . /opt/intel/oneapi/setvars.sh && \
                CMAKE_ARGS="-DGGML_SYCL=on -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx" ;; \
      cpu)      CMAKE_ARGS="" ;; \
    esac; \
    env CMAKE_ARGS="$CMAKE_ARGS" pip install --no-cache-dir -r requirements.txt


ENV PYTHONPATH=/app
CMD ["python", "app.py"]