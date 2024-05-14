def extract_comments(file_path, symbol, output_file):
    """
    Extracts comments from a code file based on the specified comment symbol and saves them to a text file.

    Args:
        file_path (str): The path to the code file from which comments will be extracted.
        symbol (str): The comment symbol used in the code file (e.g., '#' for Python, '//' for JS).
        output_file (str): The path to save the extracted comments to.

    Returns:
        str: A message indicating the result of the extraction and saving process.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            comments = [line.strip() for line in lines if line.strip().startswith(symbol)]
            with open(output_file, 'w') as out_file:
                out_file.write("\n".join(comments))
            return f"Extracted comments saved to '{output_file}'."
    except FileNotFoundError:
        return f"File '{file_path}' not found."


file_path = input("Enter the path of the code file: ")
symbol = input("Enter the comment symbol used in the code (e.g., # for Python, // for JS): ")
output_file = input("Enter the path to save the extracted comments file: ")

result = extract_comments(file_path, symbol, output_file)
print(result)
