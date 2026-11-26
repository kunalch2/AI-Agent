from retriever import load_documents

def retrieve(question):
    documents = load_documents()
    question = question.lower()

    for filename , content in documents.items():
        if question in content.lower():
            return filename, content

    return None, None