import os
from pdf_reader import read_pdf
from text_chunker import split_text_into_chunks
from translator import translate_to_spanish_with_groq, translate_to_spanish_with_xAI, translate_to_spanish_with_ollama
from file_manager import save_text_to_file
from pdf_constructor import create_pdf_from_text

def main(input_pdf_path, translations_dir, output_pdf_path):
    

    
    # Step 1: Extract text from the PDF
    text = read_pdf(input_pdf_path)
    
    # Step 2: Chunk the text into manageable pieces
    chunks = split_text_into_chunks(text)
    
    translated_chunks = []
    # Step 3: Translate each chunk and save the output
    for i, chunk in enumerate(chunks):
        print(f"procesing {i} ...") 
        # changing the function we can change the model we use to translate   
        translated_chunk = translate_to_spanish_with_xAI(chunk)
        if translated_chunk:
            chunk_file_path = os.path.join(translations_dir, f"chunk_{i+1:02d}.txt")
            save_text_to_file(translated_chunk, chunk_file_path)
        translated_chunks.append(translated_chunk)
    print("Done translating!")
    
    # Step 4: Combine translated text files into a PDF
    translated_text = "\n".join(translated_chunks)
    create_pdf_from_text(translated_text, output_pdf_path)
    print(f"Translation complete. Output PDF saved at: {output_pdf_path}")

if __name__ == "__main__":
    input_pdf_path = "input/test.pdf"
    translations_dir = "translations"
    output_pdf_path = "output/translated.pdf"
    
    main(input_pdf_path, translations_dir, output_pdf_path)
