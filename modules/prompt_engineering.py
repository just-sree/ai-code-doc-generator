def construct_prompt(parsed_data, examples):
    """
    Constructs a dynamic prompt for the LLM.

    Args:
        parsed_data (dict): Code structure.
        examples (list): Relevant examples.

    Returns:
        str: A formatted prompt string.
    """
    prompt = "You are a documentation generator. Generate high-quality documentation based on the following:\n\n"
    for example in examples:
        prompt += f"Example:\n{example}\n\n"

    prompt += "Code Structure:\n"
    for cls in parsed_data["classes"]:
        prompt += f"Class: {cls['name']}\nDocstring: {cls['docstring']}\nMethods:\n"
        for method in cls["methods"]:
            prompt += f"- {method['name']}: {method['docstring']}\n"

    for func in parsed_data["functions"]:
        prompt += f"Function: {func['name']}\nDocstring: {func['docstring']}\n"

    return prompt
