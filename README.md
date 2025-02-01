# PDF Summarizer

The PDF Summarizer is a web application built with Flask that allows users to upload a PDF file and generate a concise summary of its content. The application uses Natural Language Processing (NLP) techniques to preprocess the text, compute TF-IDF scores, and extract the most important sentences for the summary. The frontend is designed with a modern, responsive UI and includes a typing animation for the generated summary.

---

## Features

- **PDF Upload**: Users can upload PDF files directly through the web interface.
- **Text Summarization**: The application extracts text from the PDF and generates a summary using TF-IDF-based sentence scoring.
- **Typing Animation**: The summary is displayed with a simulated typing effect for a better user experience.
- **Responsive Design**: The UI is optimized for both desktop and mobile devices.
- **Loading State**: A loading indicator with an animated cursor is shown while the PDF is being processed.

---

## Technologies Used

- **Backend**:
  - Flask (Python web framework)
  - PyPDF (for extracting text from PDFs)
  - NLTK (Natural Language Toolkit for text preprocessing)
  - Scikit-learn (for TF-IDF vectorization)

- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Modern UI design with responsive layout
  - Typing animation for summary display

---

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pdf-summarizer.git
   cd pdf-summarizer
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**:
   ```bash
   python -m nltk.downloader punkt stopwords
   ```

5. **Run the Flask application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Usage

1. **Upload a PDF**:
   - Click the "Choose File" button to select a PDF file from your device.
   - Click "Upload and Summarize" to process the file.

2. **View the Summary**:
   - Once the processing is complete, the summary will be displayed with a typing animation.

---

## File Structure

```
pdf-summarizer/
├── app.py                  # Flask application
├── main.ipynb              # Jupyter Notebook for initial implementation
├── templates/              # HTML templates
│   └── index.html          # Main frontend template
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## Customization

- **Summary Length**: Modify the `top_n` parameter in the `generate_summary` function in `app.py` to change the number of sentences in the summary.
- **Styling**: Update the CSS in `templates/index.html` to customize the appearance of the application.
- **File Upload Location**: Change the `UPLOAD_FOLDER` path in `app.py` to store uploaded files in a different directory.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request with a detailed description of your changes.

---


## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [NLTK](https://www.nltk.org/) for natural language processing.
- [PyPDF](https://pypi.org/project/pypdf/) for PDF text extraction.
- [Scikit-learn](https://scikit-learn.org/) for TF-IDF vectorization.

---

## Screenshots

![upload](https://github.com/user-attachments/assets/ee374188-2793-41f9-976a-7c605d7984af)

*Upload Interface*

*Summary Display with Typing Animation*
![summary](https://github.com/user-attachments/assets/442d2b38-b3f3-4f5d-9b07-ed9aa19580a4)

---

Enjoy summarizing your PDFs with ease! 🚀
