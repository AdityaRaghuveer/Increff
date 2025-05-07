import json
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

def load_vectorstore():
    with open("app/faq_data.json") as f:
        faq_items = json.load(f)

    documents = [Document(page_content=faq["answer"], metadata={"question": faq["question"]}) for faq in faq_items]
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore
