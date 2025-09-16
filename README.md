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

## Example

| Question                       | Answer                             |
| ------------------------------ | ---------------------------------- |
| Who has React experience?      | John Doe, Jane Smith               |
| Contact info of top candidates | john@example.com, jane@example.com |

## Getting Started

```python
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings

# Load LLM and embeddings
model = OllamaLLM(model="gemma3:4b", temperature=0.5)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Initialize vector database
vector_store = Chroma(collection_name="cvs_collection", persist_directory="./chroma_langchain_db", embedding_function=embeddings)
```
