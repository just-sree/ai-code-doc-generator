from code_parser import parse_code
from retriever import retrieve_patterns
from prompt_engineering import construct_prompt
from langchain.llms import OpenAI

def generate_documentation(file_path, retriever):
    """
    Generates documentation for a Python file.

    Args:
        file_path (str): Path to the Python file.
        retriever: RAG retriever instance.

    Returns:
        str: Generated documentation.
    """
    parsed_data = parse_code(file_path)
    examples = retrieve_patterns(parsed_data, retriever)
    prompt = construct_prompt(parsed_data, examples)

    llm = OpenAI(api_key="your_openai_api_key")
    return llm(prompt)
