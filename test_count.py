import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("tech_intelligence")

print("Document count:", collection.count())
