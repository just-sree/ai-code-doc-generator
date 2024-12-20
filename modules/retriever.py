from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def retrieve_patterns(parsed_data, retriever):
    """
    Retrieve documentation examples using RAG.

    Args:
        parsed_data (dict): Code structure.
        retriever (FAISS): RAG retriever instance.

    Returns:
        list: Retrieved examples for documentation.
    """
    query = f"Document classes: {len(parsed_data['classes'])}, functions: {len(parsed_data['functions'])}"
    results = retriever.similarity_search(query, k=5)
    return [result.page_content for result in results]
