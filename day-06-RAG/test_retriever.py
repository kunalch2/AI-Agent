from retriever import load_documents
from search import retrieve

documents = load_documents()

for name, text in documents.items():
    print(name)
    print(text)
    print("-"*40)

filename, content = retrieve("Python")
print(filename)
print()
print(content)


