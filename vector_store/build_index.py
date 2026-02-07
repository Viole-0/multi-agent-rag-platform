import json
from sentence_transformers import SentenceTransformer
import chromadb

DB_PATH = "chroma_db"
COLLECTION_NAME = "tech_intelligence"

def build_vector_store():
    # Load processed documents
    with open("papers_processed.json", "r", encoding="utf-8") as f:
        docs = json.load(f)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    # ✅ CORRECT client for persistence
    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    if collection.count() > 0:
        print(f"⚠️ Collection already has {collection.count()} documents.")
        return

    texts, metadatas, embeddings, ids = [], [], [], []

    for i, doc in enumerate(docs):
        texts.append(doc["text"])
        metadatas.append(doc["metadata"])
        embeddings.append(model.encode(doc["text"]).tolist())
        ids.append(str(i))

    collection.add(
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
        ids=ids
    )

    print(f"✅ Inserted {collection.count()} documents into vector store.")

if __name__ == "__main__":
    build_vector_store()
