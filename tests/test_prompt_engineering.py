import unittest
from modules.prompt_engineering import construct_prompt

class TestPromptEngineering(unittest.TestCase):
    def setUp(self):
        # Sample parsed data and examples
        self.parsed_data = {
            "classes": [
                {
                    "name": "SampleClass",
                    "docstring": "This is a sample class.",
                    "methods": [{"name": "sample_method", "docstring": "Sample method docstring."}]
                }
            ],
            "functions": [
                {"name": "sample_function", "docstring": "This is a sample function."}
            ]
        }
        self.examples = [
            "Example documentation for a class.",
            "Example documentation for a function."
        ]

    def test_construct_prompt(self):
        prompt = construct_prompt(self.parsed_data, self.examples)
