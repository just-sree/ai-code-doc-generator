from doc_generator import generate_documentation

def main():
    import argparse

    parser = argparse.ArgumentParser(description="User interface for generating documentation.")
    parser.add_argument("file", help="Path to the Python source code file.")
    args = parser.parse_args()

    try:
        documentation = generate_documentation(args.file)
        print("Generated Documentation:\n")
        print(documentation)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()