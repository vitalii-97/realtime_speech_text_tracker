# AudioTracker

AudioTracker is a Streamlit application that allows you to upload a PDF file, display it in the browser, transcribe audio input from the microphone, and compare the transcribed text with the text extracted from the PDF.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/AudioTracker.git
   ```

2. Navigate to the project directory:

   ````shell
   cd AudioTracker
   ```

3. Install the required dependencies:

   ````shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:

   ````shell
   streamlit run app.py
   ```

2. In the web browser, you will see the AudioTracker application.

3. Upload a PDF file by clicking on the "Upload PDF" button.

4. The PDF will be displayed in the browser.

5. Click on the "Allow" button to give permission to use the microphone.

6. Start speaking, and your audio will be transcribed and displayed on the screen.

7. The transcribed text will be compared with the text extracted from the PDF, and the similarity ratio will be shown.

8. If there are any skipped lines, they will be displayed as well.

## Technologies Used

- Streamlit: A Python framework for building interactive web applications.
- PyPDF2: A library for extracting text and metadata from PDF files.
- SpeechRecognition: A library for performing speech recognition using various engines, including Google Speech Recognition.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
