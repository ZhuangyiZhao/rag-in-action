# 扫描图片型 PDF，建议用 pytesseract + pdf2image  
# sudo apt-get install tesseract-ocr
# sudo apt-get install tesseract-ocr-chi-sim

import pdf2image
import pytesseract
import os
import shutil
import pymupdf
from PIL import Image

if os.path.exists("/opt/homebrew/bin/tesseract"):
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# 创建 output 目录
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# 将 PDF 转换为图片并保存
pdf_path = '90-文档-Data/黑悟空/黑神话悟空.pdf'
if shutil.which("pdftoppm"):
    images = pdf2image.convert_from_path(pdf_path)
else:
    doc = pymupdf.open(pdf_path)
    images = []
    for page in doc:
        pix = page.get_pixmap()
        images.append(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))

for i, image in enumerate(images):
    image.save(f'{output_dir}/page_{i+1}.png')

# 使用 pytesseract 提取文本
available_langs = set(pytesseract.get_languages(config=""))
ocr_lang = "chi_sim" if "chi_sim" in available_langs else "eng"
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang=ocr_lang)
    print(f"第 {i+1} 页文本:")
    print(text)
    print("\n") 
