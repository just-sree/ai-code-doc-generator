import ast

def parse_code(file_path):
    """
    Parses a Python file to extract classes, functions, and docstrings.

    Args:
        file_path (str): Path to the Python file.

    Returns:
        dict: Parsed structure including classes and functions.
    """
    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)
    parsed_structure = {"classes": [], "functions": []}

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = [
                {"name": method.name, "docstring": ast.get_docstring(method)}
                for method in node.body if isinstance(method, ast.FunctionDef)
            ]
            parsed_structure["classes"].append({
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "methods": methods
            })
        elif isinstance(node, ast.FunctionDef):
            parsed_structure["functions"].append({
                "name": node.name,
                "docstring": ast.get_docstring(node)
            })

    return parsed_structure
