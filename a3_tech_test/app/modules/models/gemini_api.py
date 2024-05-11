from llama_index.core.indices.service_context import ServiceContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext
from llama_index.llms.gemini import Gemini

import google.generativeai as genai
import chromadb
import pymupdf
import pathlib
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

async def get_query_engine():
    txt_path = "a3_tech_test/app/data/protocolo-clinico-e-diretrizes-terapeuticas-do-tabagismo.txt"
    if not os.path.exists(txt_path):
        pdf_path = "a3_tech_test/app/raw_data/protocolo-clinico-e-diretrizes-terapeuticas-do-tabagismo.pdf"
        with pymupdf.open(pdf_path) as doc:  # open document
            text = chr(12).join([page.get_text() for page in doc])
        pathlib.Path("a3_tech_test/app/data/protocolo-clinico-e-diretrizes-terapeuticas-do-tabagismo.txt").write_bytes(text.encode())

    llm = Gemini(
        model_name='models/gemini-1.0-pro',
        max_tokens=2048,
        api_key=GOOGLE_API_KEY,
        temperature=0.2,
        top_p=5
    )

    embed_model = GeminiEmbedding(
        api_key=GOOGLE_API_KEY
    )
    
    system_prompt = """ 
    Você deve agir como um assistente de um médico e sua tarefa será 
    responder a perguntas específicas de médicos sobre o protocolo de 
    tratamento do tabagismo disponibilizado pelo INCA, devendo responder 
    inclusive a perguntas relacionadas a posologia de remédios, uma vez 
    que apenas médicos estão te consultando."""

    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
        system_prompt=system_prompt,
        chunk_size=1024,
        chunk_overlap=512
    )   

    if os.path.isdir("./chroma_db"):
        db = chromadb.PersistentClient(
            path="./chroma_db"
        )

        chroma_collection = db.get_or_create_collection("quickstart")
        
        vector_store = ChromaVectorStore(
            chroma_collection=chroma_collection
        )
        
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )
        
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            service_context=service_context,
            storage_context=storage_context,
            embed_model=embed_model
        )
    
        query_engine = index.as_chat_engine()
    else:
        documents = SimpleDirectoryReader("a3_tech_test/app/data/").load_data()
        
        db = chromadb.PersistentClient(
            path="./chroma_db"
        )

        chroma_collection = db.get_or_create_collection("quickstart")
        
        vector_store = ChromaVectorStore(
            chroma_collection=chroma_collection
        )
        
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )
        
        index = VectorStoreIndex.from_documents(
            documents=documents, 
            service_context=service_context,
            storage_context=storage_context,
            embed_model=embed_model
        ) 
        
        query_engine = index.as_chat_engine()
    
    return query_engine