from PyPDF2 import PdfReader
import re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from summarizer import Summarizer

def read_pdf(file_path):
    try:
        # Open the PDF file
        pdf_file = open(file_path, "rb")

        # Create a PDF reader object
        pdf_reader = PdfReader(pdf_file)

        # Read the content from the PDF
        pdf_content = ""
        for page in pdf_reader.pages:
            pdf_content += page.extract_text()

        # Close the PDF file
        pdf_file.close()

        return pdf_content
    except Exception as e:
        print("An error occurred while reading the PDF:", str(e))
        return None

def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^A-Za-z. ]+', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Join the words back into sentences
    cleaned_text = ' '.join(filtered_words)

    return cleaned_text

if __name__ == "__main__":
    # Specify the path to the PDF file
    pdf_file_path = "Operations Management.pdf"

    # Step 1: Read the PDF content
    pdf_content = read_pdf(pdf_file_path)

    if pdf_content:
        # Step 2: Text Preprocessing
        preprocessed_text = clean_text(pdf_content)

        # Step 3: Text Summarization using BERT
        model = Summarizer()
        summary = model(preprocessed_text)

        # Step 4: Print the summary
        print(summary)

        print("Summary generated successfully.")
    else:
        print("PDF reading failed. Please check the PDF file path.")
