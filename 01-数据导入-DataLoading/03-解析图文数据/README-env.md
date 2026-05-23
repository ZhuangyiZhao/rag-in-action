# 图文数据解析专用环境

这个目录使用独立虚拟环境，避免把图片、PPT、PDF 解析相关依赖装到全局 Python。

## 激活

```bash
cd "/Users/zhuangyi.zhao/Library/Mobile Documents/com~apple~CloudDocs/AI/RAG/code/rag-in-action"
source "01-数据导入-DataLoading/03-解析图文数据/.venv/bin/activate"
```

## 安装或重建

```bash
cd "01-数据导入-DataLoading/03-解析图文数据"
/opt/homebrew/bin/python3.12 -m venv --clear .venv
.venv/bin/python -m pip install --upgrade pip setuptools wheel
.venv/bin/python -m pip install -r requirements-vision-docs.txt
.venv/bin/python -m nltk.downloader -d .venv/nltk_data punkt_tab averaged_perceptron_tagger_eng
```

## 系统依赖

这些不是 Python 包，需要按系统安装：

- `01-Unstructured读图.py`: 图片 OCR 通常需要 Tesseract。
- `02-Unstructured读PPT.py`: PPT 解析需要 LibreOffice 的 `soffice` 命令。
- `03-大模型读取图文.py`: `pdf2image` 需要 Poppler，并且 OpenAI 调用需要配置 `OPENAI_API_KEY`。

Mac 可用 Homebrew 安装：

```bash
brew install tesseract poppler
brew install --cask libreoffice
```

## 运行示例

这些脚本里的数据路径是按项目根目录写的，所以建议从 `rag-in-action` 根目录运行：

```bash
cd "/Users/zhuangyi.zhao/Library/Mobile Documents/com~apple~CloudDocs/AI/RAG/code/rag-in-action"
export HF_HOME="01-数据导入-DataLoading/03-解析图文数据/.venv/hf_cache"
export MPLCONFIGDIR="01-数据导入-DataLoading/03-解析图文数据/.venv/mpl_cache"
export XDG_CACHE_HOME="01-数据导入-DataLoading/03-解析图文数据/.venv/xdg_cache"
"01-数据导入-DataLoading/03-解析图文数据/.venv/bin/python" "01-数据导入-DataLoading/03-解析图文数据/01-Unstructured读图.py"
```
