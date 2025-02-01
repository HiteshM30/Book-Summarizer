from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from pypdf import PdfReader
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_text(text):
    swords = set(nltk.corpus.stopwords.words('english'))
    stemmer = PorterStemmer()
    sentences = sent_tokenize(text)
    preprocess_sent = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [stemmer.stem(word) for word in words if word.isalnum() and word not in swords]
        preprocess_sent.append(' '.join(words))
    return preprocess_sent

def compute_tfidf(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    return tfidf_matrix

def score_sentences(tfidf_matrix):
    sentence_scores = tfidf_matrix.sum(axis=1)
    return sentence_scores

def generate_summary(text, top_n=None):
    sentences = sent_tokenize(text)
    total_sentences = len(sentences)
    
    if top_n is None:
        # Default to 10% of the sentences, but at least 3 and at most 10
        top_n = max(3, min(10, int(total_sentences * 0.1)))
    preprocessed_sentences = preprocess_text(text)
    tfidf_matrix = compute_tfidf(preprocessed_sentences)
    sentence_scores = score_sentences(tfidf_matrix)
    
    ranked_sentences = [sent for _, sent in sorted(zip(sentence_scores, sent_tokenize(text)), reverse=True)]
    summary = ' '.join(ranked_sentences[:top_n])
    
    return summary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            reader = PdfReader(filepath)
            text = ''
            for i in range(3, len(reader.pages)):
                page = reader.pages[i]
                text += page.extract_text()
            
            summary = generate_summary(text)
            return render_template('index.html', summary=summary)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)