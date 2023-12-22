import fitz
import pandas as pd


def extract_blocks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages_text = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")
        page_texts = [block[4] for block in blocks]  # 提取每个块的文本
        pages_text.append(page_texts)

    doc.close()
    return pages_text


def pages_to_dataframe(pages_text):
    data = []

    for page_texts in pages_text:
        row = {f'text{i + 1}': text for i, text in enumerate(page_texts)}
        data.append(row)

    df = pd.DataFrame(data)
    return df


pdf_path = 'D:\SSV Mens Labels.pdf'
pages_text = extract_blocks_from_pdf(pdf_path)
df = pages_to_dataframe(pages_text)

# 保存到Excel
df.to_excel('output.xlsx', index=False)
