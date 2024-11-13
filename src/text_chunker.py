# text_chunker.py
import re

def split_text_into_chunks(text, max_words=800):
    """
    Splits the given text into chunks of a specified word count range.

    Parameters:
    text (str): The text to be split into chunks.
    max_words (int): The maximum number of words per chunk.

    Returns:
    list: A list of text chunks.
    """
    # Split text into sentences using regex pattern that looks for punctuation followed by space
    sentences = re.split(r'(?<=[.!?]) +', text)
    # Initialize list to store final chunks and current chunk being built
    chunks = []
    current_chunk = []

    # Process each sentence
    for sentence in sentences:
        # Add current sentence to the current chunk
        current_chunk.append(sentence)
        # If current chunk exceeds max words, join it and add to chunks list
        if sum(len(s.split()) for s in current_chunk) >= max_words:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
    
    # Add any remaining sentences in the current chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    # Return the list of text chunks
    return chunks