def parse_code(file_path):
    """
    Parses the source code file to extract structure and comments.

    Args:
        file_path (str): Path to the source code file.

    Returns:
        dict: A dictionary containing classes, functions, and their respective docstrings.
    """
    import ast

    # Read the source code file
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")

    # Parse the source code into an abstract syntax tree (AST)
    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        raise SyntaxError(f"Syntax error in the file: {file_path}. Error: {e}")

    # Initialize containers for parsed data
    parsed_data = {
        "classes": [],
        "functions": [],
    }

    # Define a helper function to extract docstrings
    def extract_docstring(node):
        return ast.get_docstring(node) if ast.get_docstring(node) else "No docstring provided."

    # Walk through the AST to extract classes and functions
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            parsed_data["classes"].append({
                "name": node.name,
                "docstring": extract_docstring(node),
                "methods": [
                    {
                        "name": method.name,
                        "docstring": extract_docstring(method),
                    }
                    for method in node.body if isinstance(method, ast.FunctionDef)
                ]
            })
        elif isinstance(node, ast.FunctionDef):
            parsed_data["functions"].append({
                "name": node.name,
                "docstring": extract_docstring(node),
            })

    return parsed_data

if __name__ == "__main__":
    import json
    import argparse

    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Parse a Python file and extract its structure and comments.")
    parser.add_argument("file", help="Path to the Python source code file.")
    args = parser.parse_args()

    # Parse the file and output the results
    try:
        parsed_structure = parse_code(args.file)
        print(json.dumps(parsed_structure, indent=4))
    except Exception as e:
        print(f"Error: {e}")