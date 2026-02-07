import chromadb

DB_PATH = "chroma_db"

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_collection("tech_intelligence")

def retrieve_docs(query: str, k: int = 5, return_metadata=False):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    if return_metadata:
        return docs, metas

    return docs
