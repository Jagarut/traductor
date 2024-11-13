import os

def save_text_to_file(chunk, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(chunk)

def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
