import fitz  # PyMuPDF

def read_pdf(file_path):
    """
    Reads a PDF file and extracts the text from each page.

    Parameters:
    file_path (str): The path to the PDF file.

    Returns:
    str: The extracted text from the PDF.
    """
    # Open the PDF document
    doc = fitz.open(file_path)
    text = ""

    # Iterate through each page in the document
    for page_num in range(len(doc)):
        # Load the page
        page = doc.load_page(page_num)
        # Extract the text from the page and append it to the text variable
        text += page.get_text()

    doc.close()
    return text
