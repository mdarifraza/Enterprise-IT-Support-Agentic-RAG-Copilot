from app.services.ingestion import load_file,chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents


docs = load_file(Path("F:/Enterprise-IT-Support-Agentic-RAG-Copilot/data/sample_kb/company_it_handbook.md"))
chunks= chunk_documents(docs)

add_documents(chunks)