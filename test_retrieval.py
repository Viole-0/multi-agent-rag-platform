from agents.retrieval_agent import retrieve_docs

query = "parameter efficient fine tuning in large language models"

docs = retrieve_docs(query)

print("\nRetrieved Documents:\n")
for i, doc in enumerate(docs, 1):
    print(f"{i}. {doc[:200]}...\n")
