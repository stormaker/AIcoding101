import os
from dotenv import load_dotenv

from langchain.chains.combine_documents.refine import RefineDocumentsChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
openai_api = os.getenv("OPENAI_API_KEY")

# Step 1: Read the text file and split into chunks
with open("input.txt", "r", encoding='utf-8') as f:
	 text = f.read()

text_splitter = RecursiveCharacterTextSplitter()
chunks = text_splitter.split_text(text)

# Step 2: Initialize the LLM chain
llm_chain = OpenAI()

#prompt_template = PromptTemplate("你是会议记录整理人员，以下是一段录音的逐字稿，请逐字将其整理成前后连贯的文字，需要注意：1.保留完整保留原始录音的所有细节。2.尽量保留原文语义、语感。3.请修改错别字，符合中文语法规范。4.去掉说话人和时间戳。5.第一人称：我。6.请足够详细，字数越多越好。7.保持原始录音逐字稿的语言风格.")

prompt_template = PromptTemplate.from_template("你是会议记录整理人员，以下是一段录音的逐字稿，请逐字将其整理成前后连贯的文字，需要注意：1.保留完整保留原始录音的所有细节。2.尽量保留原文语义、语感。3.请修改错别字")

summary_chain = RefineDocumentsChain(
	initial_llm_chain=llm_chain,
	refine_llm_chain=llm_chain,
	document_prompt=prompt_template,
	document_variable_name="chunks",
	initial_response_name="prev_response"
)


refined_summaries = []
for chunk in chunks:
	refined_summary = summary_chain({"chunks": chunk}, return_only_outputs=True)["output_text"]
	refined_summaries.append(refined_summary)


with open("output.txt", "w") as file:
	for summary in refined_summaries:
		file.write(summary + "\n")