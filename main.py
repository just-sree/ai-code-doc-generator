from doc_generator import generate_documentation
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def main():
    retriever = FAISS.load_local("faiss_index", OpenAIEmbeddings())
    file_path = "data/sample_code.py"
    documentation = generate_documentation(file_path, retriever)
    print(documentation)

if __name__ == "__main__":
    main()
