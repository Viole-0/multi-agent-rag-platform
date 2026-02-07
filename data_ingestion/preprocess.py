import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

def preprocess():
    with open("papers_raw.json", "r", encoding="utf-8") as f:
        papers = json.load(f)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    documents = []

    for paper in papers:
        chunks = splitter.split_text(paper["summary"])
        for chunk in chunks:
            documents.append({
                "text": chunk,
                "metadata": {
                    "title": paper["title"],
                    "published": paper["published"]
                }
            })

    with open("papers_processed.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print("✅ Papers preprocessed for RAG.")

if __name__ == "__main__":
    preprocess()
