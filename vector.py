from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import glob 
from langchain_community.document_loaders import PyPDFLoader


# Embedding model
embeddings =OllamaEmbeddings(model="mxbai-embed-large")

db_location ="./chroma_langchain_db"
pdf_folder ="CVs"
add_documents = not os.path.exists(db_location)

if add_documents :
    documents =[]
    ids = []
    # Charger chaque PDF du dossier 
    for file_path in glob.glob(os.path.join(pdf_folder, "*.pdf")):
        loader = PyPDFLoader(file_path)
        pages =loader.load()
        for i, page in enumerate(pages) :
            document =Document(
                page_content=page.page_content ,
                metadata={"source": file_path, "page": i}
            )
            documents.append(document)
            ids.append(f"{file_path}_{i}")

# Créer la base de données vectorielle Chroma
print("Creating or loading vector store...")
vector_Store = Chroma(
    collection_name="cvs_collection",
    persist_directory=db_location,
    embedding_function=embeddings,
)

# Ajouter les documents à la base de données si c'est la première fois
print("Adding documents to vector store..." if add_documents else "Vector store already exists, skipping document addition.")
if add_documents:
    vector_Store.add_documents(documents=documents, ids=ids)
print("Vector store is ready. Start Retriver ...")    
# Creer un retriver pour interroger la base de données
retriever = vector_Store.as_retriever(
    search_kwargs={"k": 3}  # Nombre de documents similaires à récupérer
)
print("Retriever is ready.")
