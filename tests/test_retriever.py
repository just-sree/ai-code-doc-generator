import unittest
from modules.retriever import retrieve_patterns
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

class TestRetriever(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Build a temporary FAISS index for testing
        examples = [
            Document(page_content="Class documentation example."),
            Document(page_content="Function documentation example."),
            Document(page_content="Method documentation example."),
        ]
        embeddings = OpenAIEmbeddings()
        cls.retriever = FAISS.from_documents(examples, embeddings)

    def test_retrieve_patterns(self):
        # Mock parsed data
        parsed_data = {"classes": [{"name": "TestClass"}], "functions": [{"name": "test_function"}]}
        results = retrieve_patterns(parsed_data, self.retriever)
        self.assertTrue(len(results) > 0)
        self.assertIn("Class documentation example.", results)

if __name__ == "__main__":
    unittest.main()
