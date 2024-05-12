from llama_index.core.indices.service_context import ServiceContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext
)
from llama_index.llms.gemini import Gemini

import google.generativeai as genai
import chromadb
import pymupdf
import pathlib
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PERSIST_DIR = "./chroma_db"

genai.configure(api_key=GOOGLE_API_KEY)


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
    top_p=0.3
)

embed_model = GeminiEmbedding(
    api_key=GOOGLE_API_KEY
)

system_prompt = """ 
Você é um médico especializado em tabagismo. Você analisa casos de tabagismo e utiliza o 
protocolo clínico e diretrizes terapeuticas do tabagisto fornecido pelo 
INCA (Instituto Nacional de Câncer). 
Seu papel é se comunicar de forma informativa com seus pacientes.
Responda à todas perguntas somente e necessariamente em português. 
Suas ações devem seguir as seguintes regras:
1 - Suas respostas devem ser o mais informativas possíveis.
2 - Suas respostas devem se basear estritamente no que consta no protocolo clínico do INCA.
"""

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    system_prompt=system_prompt,
    chunk_size=1024,
    chunk_overlap=512
)   

if os.path.exists(PERSIST_DIR):
    db = chromadb.PersistentClient(
        path=PERSIST_DIR
    )

    chroma_collection = db.get_collection("embeddings")
    
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

else:
    print("entrei else usando documentos")
    documents = SimpleDirectoryReader("a3_tech_test/app/data/").load_data()
   
    db = chromadb.PersistentClient(
        path=PERSIST_DIR
    )

    chroma_collection = db.create_collection("embeddings")
    
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

    
query_engine = index.as_query_engine()