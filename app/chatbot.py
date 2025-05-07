from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.memory import memory
import os

def load_chain():
    from app.data_loader import load_vectorstore
    vectorstore = load_vectorstore()
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-4") 
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        return_source_documents=True
    )
    return qa_chain
