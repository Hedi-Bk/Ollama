# Agentic AI CV Analyzer

An intelligent assistant designed for recruiters to analyze CVs automatically. Upload your CVs in PDF format, ask questions, and get insights extracted directly from the documents — no manual data processing required.

## Features

- **CV Analysis Agent**: Automatically reads and interprets CVs, providing structured answers.
- **Semantic Search**: Uses Chroma vector database to retrieve the most relevant CV segments.
- **Embeddings & LLM**:
  - Embeddings: `OllamaEmbeddings(model="mxbai-embed-large")`
  - LLM: `OllamaLLM(model="gemma3:4b", temperature=0.5)` for natural language answers.
- **Dynamic Responses**: Answers recruiter queries directly from the CV content.
- **Scalable**: Handles multiple CVs efficiently with chunking and vector search.

## How it works

1. Upload CVs in PDF format to the `CVs` folder.
2. The system splits the CVs into chunks.
3. Chunks are stored in a **Chroma vector database**.
4. Recruiter asks questions via the prompt.
5. Ollama LLM generates answers based solely on the CVs.

<img width="676" height="453" alt="image8" src="https://github.com/user-attachments/assets/28efe62c-c477-4df3-a4c9-c05a092cafeb" />


## Example

| Question                       | Answer                             |
| ------------------------------ | ---------------------------------- |
| Who has React experience?      | John Doe, Jane Smith               |
| Contact info of top candidates | john@example.com, jane@example.com |

## 🔧 Models Used & Architecture

**1. LLM (Local Language Model) – Ollama**  
- **Model name:** `gemma3:4b`  
- **Purpose:** Text generation and understanding RAG prompts  
- **Settings:** `temperature = 0.5` → balance between creativity and precision  

**2. Embeddings – Ollama Embeddings**  
- **Model name:** `mxbai-embed-large`  
- **Purpose:** Convert CVs/documents into vectors for semantic search  

**3. Vector Database – Chroma**  
- **Collection name:** `cvs_collection`  
- **Directory:** `./chroma_langchain_db`  
- **Purpose:** Store embeddings for fast retrieval during RAG queries  

---
