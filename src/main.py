import os
from src.pdf_reader import read_pdf
from src.text_chunker import split_text_into_chunks
from src.translator import translate_to_spanish
from src.file_manager import save_chunk_to_file, create_directory_if_not_exists
from src.pdf_constructor import create_pdf_from_text

def main():
    input_pdf_path = "input/original.pdf"
    translations_dir = "translations"
    output_pdf_path = "output/translated.pdf"

    create_directory_if_not_exists(translations_dir)

    text = read_pdf(input_pdf_path)
    chunks = split_text_into_chunks(text)

    translated_chunks = []
    for i, chunk in enumerate(chunks):
        translated_chunk = translate_to_spanish(chunk)
        chunk_file_path = os.path.join(translations_dir, f"chunk_{i+1:02d}.txt")
        save_chunk_to_file(translated_chunk, chunk_file_path)
        translated_chunks.append(translated_chunk)

    translated_text = "\n".join(translated_chunks)
    create_pdf_from_text(translated_text, output_pdf_path)

if __name__ == "__main__":
    main()
