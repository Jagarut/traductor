import os

def save_chunk_to_file(chunk, file_path):
    with open(file_path, 'w') as file:
        file.write(chunk)

def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
