from app.core.config import get_settings

settings=get_settings()
print(f"App Name: {settings.app_name}")
print(f"App Environment: {settings.app_env}")
print(f"Gemini API Key: {settings.gemini_api_key}")
print(f"Tavily API Key: {settings.tavily_api_key}")
print(f"Pinecone API Key: {settings.pinecone_api_key}")
print(f"Pinecone Index Name: {settings.pinecone_index_name}")
print(f"Pinecone Namespace: {settings.pinecone_namespace}")
print(f"Embedding Model: {settings.embedding_model}")
print(f"Gemini Model: {settings.gemini_model}")