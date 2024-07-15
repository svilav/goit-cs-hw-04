def create_test_files():
    files_content = {
        'file1.txt': "This is a test file. It contains some text for testing purposes. Here are some keywords: error, warning, failed.",
        'file2.txt': "Another test file. This file also contains some text. Keywords might be here: warning, success, finished.",
        'file3.txt': "This is the third test file. More test content inside. Look for these keywords: error, success, passed."
    }

    for file_name, content in files_content.items():
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Created file {file_name}")
        except Exception as e:
            print(f"Error creating {file_name}: {e}")


if __name__ == "__main__":
    create_test_files()
