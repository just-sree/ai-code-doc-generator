from code_parser import parse_code
from rag_retriever import retrieve_patterns

def generate_documentation(file_path):
    """
    Generates human-readable documentation for the given source code file.

    Args:
        file_path (str): Path to the source code file.

    Returns:
        str: Generated documentation.
    """
    parsed_data = parse_code(file_path)
    patterns = retrieve_patterns(parsed_data)

    documentation = "# Documentation\n\n"
    for cls in parsed_data.get("classes", []):
        documentation += f"## Class: {cls['name']}\n\n{cls['docstring']}\n\n"
        for method in cls["methods"]:
            documentation += f"### Method: {method['name']}\n\n{method['docstring']}\n\n"

    for func in parsed_data.get("functions", []):
        documentation += f"## Function: {func['name']}\n\n{func['docstring']}\n\n"

    documentation += "# Documentation Patterns\n\n"
    for pattern in patterns:
        documentation += f"- {pattern}\n"

    return documentation

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate documentation for a Python source code file.")
    parser.add_argument("file", help="Path to the Python source code file.")
    args = parser.parse_args()

    try:
        documentation = generate_documentation(args.file)
        print(documentation)
    except Exception as e:
        print(f"Error: {e}")
