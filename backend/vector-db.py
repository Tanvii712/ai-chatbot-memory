from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_vector_db():
    return Chroma(
        collection_name="chat_memory",
        embedding_function=OpenAIEmbeddings()
    )