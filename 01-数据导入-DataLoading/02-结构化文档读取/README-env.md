# 结构化文档读取专用环境

这个目录使用独立虚拟环境，避免安装整套 LangChain/GPU/Gradio 依赖。

## 激活

```bash
cd "/Users/zhuangyi.zhao/Library/Mobile Documents/com~apple~CloudDocs/AI/RAG/code/rag-in-action"
source "01-数据导入-DataLoading/02-结构化文档读取/.venv/bin/activate"
```

## 安装或重建

```bash
cd "01-数据导入-DataLoading/02-结构化文档读取"
/opt/homebrew/bin/python3.12 -m venv --clear .venv
.venv/bin/python -m pip install --upgrade pip setuptools wheel
.venv/bin/python -m pip install -r requirements-structured-docs.txt
.venv/bin/python -m nltk.downloader -d .venv/nltk_data punkt_tab averaged_perceptron_tagger_eng
```

## 运行示例

这些脚本里的数据路径是按项目根目录写的，所以建议从 `rag-in-action` 根目录运行：

```bash
cd "/Users/zhuangyi.zhao/Library/Mobile Documents/com~apple~CloudDocs/AI/RAG/code/rag-in-action"
"01-数据导入-DataLoading/02-结构化文档读取/.venv/bin/python" "01-数据导入-DataLoading/02-结构化文档读取/01-LangChain-TextLoader-JSON.py"
```
