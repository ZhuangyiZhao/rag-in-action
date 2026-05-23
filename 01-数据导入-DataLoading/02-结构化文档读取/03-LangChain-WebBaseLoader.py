# 使用WebBaseLoader加载网页
import os

os.environ.setdefault("USER_AGENT", "rag-in-action-structured-docs/1.0")

import bs4
from langchain_community.document_loaders import WebBaseLoader
page_url = "https://zh.wikipedia.org/wiki/黑神话：悟空"
headers = {"User-Agent": "rag-in-action-structured-docs/1.0"}
# loader = WebBaseLoader(web_paths=[page_url])
# docs = []
# docs = loader.load()
# assert len(docs) == 1
# doc = docs[0]
# print(f"{doc.metadata}\n")
# print(doc.page_content.strip()[:3000])


# 只解析文章的主体部分
loader = WebBaseLoader(
    web_paths=[page_url],
    header_template=headers,
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(id="bodyContent"),
    },
    # bs_get_text_kwargs={"separator": " | ", "strip": True},  # 提取网页文本时，把各块文字用 " | " 分隔，并清理多余空白
)
docs = []
docs = loader.load()
assert len(docs) == 1
doc = docs[0]
print(f"{doc.metadata}\n")
print(doc.page_content)
