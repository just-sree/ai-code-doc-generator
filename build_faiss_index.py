from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

def build_faiss_index():
    """
    Build and save a FAISS index using predefined documentation patterns.
    """
    # Define documentation examples as a list of `Document` objects
    examples = [
        Document(page_content="Class: A template for classes in Python."),
        Document(page_content="Function: A template for functions in Python."),
        Document(page_content="Method: A template for methods inside classes."),
        Document(page_content="Usage examples: Include code snippets and explanations."),
        Document(page_content="Arguments: Clearly describe parameters and types."),
        Document(page_content="Return: Specify return type and details."),
    ]

    # Initialize OpenAI embeddings and FAISS
    embeddings = OpenAIEmbeddings()  # Ensure API key is set in your environment
    faiss_index = FAISS.from_documents(examples, embeddings)

    # Save the FAISS index locally
    faiss_index.save_local("faiss_index")
    print("FAISS index created and saved successfully!")

if __name__ == "__main__":
    build_faiss_index()
