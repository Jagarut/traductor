def split_text_into_chunks(text, min_words=300, max_words=800):
    """
    Splits the given text into chunks of a specified word count range.

    Parameters:
    text (str): The text to be split into chunks.
    min_words (int): The minimum number of words per chunk.
    max_words (int): The maximum number of words per chunk.

    Returns:
    list: A list of text chunks.
    """
    # Split the text into individual words
    words = text.split()
    chunks = []
    current_chunk = []

    # Iterate through each word in the text
    for word in words:
        # Add the word to the current chunk
        current_chunk.append(word)
        # If the current chunk's word count is within the specified range, add it to the chunks list
        if len(current_chunk) >= min_words and len(current_chunk) <= max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    # Add any remaining words as the final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
