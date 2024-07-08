import streamlit as st
import easyocr
from PIL import Image
import fitz  # PyMuPDF
import io

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

def perform_ocr(image):
    result = reader.readtext(image)
    extracted_text = ' '.join([text[1] for text in result])
    return extracted_text

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def get_html_content(text_content, access_key):
    # Read HTML template from the file
    with open('readaloud.html', 'r', encoding='utf-8') as file:
        html_template = file.read()

    # Replace placeholders with actual values
    html_code = html_template.replace('{{ text_content }}', text_content).replace('{{ access_key }}', access_key)
    return html_code

def display_html(text_content, access_key):
    html_content = get_html_content(text_content, access_key)
    st.components.v1.html(html_content, height=600, scrolling=True)

def main():
    st.title("Reading Assistance")

    st.header("Option 1: Enter Text Manually")
    text_input = st.text_area("Type your text here:")
    st.write("or")

    st.header("Option 2: Upload an Image")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    extracted_text = ""
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        extracted_text = perform_ocr(image)
        st.subheader("Extracted Text:")
        st.write(extracted_text)

    st.write("or")

    st.header("Option 3: Upload a PDF")
    uploaded_pdf = st.file_uploader("Choose a PDF...", type=["pdf"])

    pdf_text = ""
    if uploaded_pdf is not None:
        pdf_text = extract_text_from_pdf(uploaded_pdf)
        st.subheader("Extracted Text from PDF:")
        st.write(pdf_text)

    # Combine text inputs
    combined_text = "\n".join(filter(None, [text_input, extracted_text, pdf_text]))

    if combined_text:
        st.subheader("Text for Text-to-Speech:")
        st.write(combined_text)

        # Display the HTML component with the combined text
        access_key = 'F4nLejAZww7_NC1DB8SF7pf0CKQLQhr9kBaZ0w9TISI'  # Replace with your actual Unsplash API access key
        display_html(combined_text, access_key)

if __name__ == "__main__":
    main()
