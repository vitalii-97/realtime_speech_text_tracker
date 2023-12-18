import streamlit as st
import base64
import difflib
import PyPDF2
import speech_recognition as sr

# Setting Webpage Configurations
st.set_page_config(page_icon="🎤", page_title="AudioTracker", layout="wide")
st.title(":rainbow[Audio Tracker]🔊")
st.divider()


def main():
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file is not None:
        pdf_url = get_pdf_url(uploaded_file)
        embed_code = get_embed_code(pdf_url)
        # Display the PDF
        st.markdown(embed_code, unsafe_allow_html=True)
        st.write(" 🤖 Please speak and I will transcribe your audio:")
        transcribed_text = transcribe_audio()
        st.write("Transcribed Text:")
        st.write(transcribed_text)
        compare_text_with_pdf(transcribed_text, uploaded_file)


def get_pdf_url(uploaded_file):
    pdf_data = uploaded_file.read()
    pdf_url = f"data:application/pdf;base64,{base64.b64encode(pdf_data).decode()}"
    return pdf_url


def get_embed_code(pdf_url):
    embed_code = f'<embed src="{pdf_url}" type="application/pdf" width="100%" height="600px" />'
    return embed_code


def transcribe_audio():
    recognizer = sr.Recognizer()
    # Set the microphone as the audio source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.write("Listening...")
        # Continuously listen for audio until interrupted
        while True:
            try:
                audio = recognizer.listen(source, phrase_time_limit=10)  # Limit each transcription to 10 seconds
                transcribed_text = recognizer.recognize_google(audio)
                st.write(transcribed_text)
            except sr.UnknownValueError:
                st.write("Sorry, I could not understand your audio.")
            except sr.RequestError as e:
                st.write(f"Error: {e}")
            except KeyboardInterrupt:
                st.write("Transcription stopped.")
                break


def compare_text_with_pdf(transcribed_text, uploaded_file):
    pdf_data = uploaded_file.read()
    original_text = extract_text_from_pdf(pdf_data)
    if original_text and transcribed_text:
        similarity_ratio = difflib.SequenceMatcher(None, original_text, transcribed_text).ratio()
        st.write(f"Similarity Ratio: {similarity_ratio}")
        original_lines = original_text.split("\n")
        transcribed_lines = transcribed_text.split("\n")
        skipped_lines = []
        for line in original_lines:
            if line not in transcribed_lines:
                skipped_lines.append(line)
        if skipped_lines:
            st.warning("Skipped Lines:")
            for line in skipped_lines:
                st.write(line)


def extract_text_from_pdf(pdf_data):
    pdf_data = "pdf/1.pdf"
    # Add your logic to extract text from the PDF using your preferred library
    # For example, you can use PyPDF2 or pdfplumber
    # Here's an example using PyPDF2
    with open(pdf_data, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        text = ""
        for page_num in range(total_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        print(text)
        return text


if __name__ == "__main__":
    main()