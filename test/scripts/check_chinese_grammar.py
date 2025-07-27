import os
import pycorrector
from pathlib import Path

def check_grammar_in_file(file_path):
    """Check grammar in a single file and return errors."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    errors = pycorrector.detect(text)
    return errors

def main():
    directories = ['docs', 'docs/proposal']
    error_found = False
    error_messages = []

    for directory in directories:
        for file_path in Path(directory).rglob('*.md'):  # Adjust for .txt or other extensions if needed
            if file_path.is_file():
                print(f"Checking file: {file_path}")
                errors = check_grammar_in_file(file_path)
                if errors:
                    error_found = True
                    error_messages.append(f"Grammar errors in {file_path}:")
                    for error in errors:
                        error_messages.append(f" - {error}")
                else:
                    print(f"No grammar errors found in {file_path}")

    if error_found:
        print("\nGrammar errors found:")
        for msg in error_messages:
            print(msg)
        exit(1)  # Exit with error code to fail the workflow
    else:
        print("\nNo grammar errors found in any files.")
        exit(0)  # Exit successfully

if __name__ == "__main__":
    main()