# PDF Translator

This program reads a PDF file, splits the text into manageable chunks, translates each chunk into Spanish using various translation APIs, and then combines the translated text into a new PDF file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/pdf-translator.git
   cd pdf-translator
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   XAI_API_KEY=your_xai_api_key
   ```

## Usage

1. Place your input PDF file in the `input` directory.
2. Run the main script:
   ```sh
   python src/main.py
   ```

The program will:
- Read the PDF file from the `input` directory.
- Split the text into chunks.
- Translate each chunk into Spanish using the specified translation API.
- Save the translated chunks as text files in the `translations` directory.
- Combine the translated text into a new PDF file and save it in the `output` directory.

## Dependencies

- `fpdf`: For creating PDF files.
- `PyMuPDF`: For reading PDF files.
- `requests`: For making HTTP requests to translation APIs.
- `openai`: For interacting with the OpenAI API.
- `python-dotenv`: For loading environment variables from a `.env` file.

You can install these dependencies using the following command:
