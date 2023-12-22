import fitz
import pandas as pd


def extract_blocks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_blocks = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")
        all_blocks.extend(blocks)

    doc.close()
    return all_blocks


def blocks_to_dataframe(blocks):
    data = []
    max_length = max(len(block) for block in blocks)  # 获取块中元素数量的最大值

    # 创建列名
    columns = [f'col_{i}' for i in range(max_length)]

    for block in blocks:
        row = [item for item in block]
        data.append(row)

    df = pd.DataFrame(data, columns=columns)
    return df


pdf_path = 'D:\SSV Mens Labels.pdf'
blocks = extract_blocks_from_pdf(pdf_path)
df = blocks_to_dataframe(blocks)

# 保存到Excel
df.to_excel('output.xlsx', index=False)
