import fitz  

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text content from a given PDF file path.

    Args:
        pdf_path: The file path to the PDF document.

    Returns:
        A string containing all the extracted text.
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        return text
    except FileNotFoundError:
        return f"Error: PDF file not found at {pdf_path}"
    except Exception as e:
        return f"An error occurred during PDF processing: {e}"

if __name__ == '__main__':
    # Simple test (assuming a test file exists)
    # print(extract_text_from_pdf("../data/sample_resume.pdf"))
    pass