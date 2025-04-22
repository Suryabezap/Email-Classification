import re
import pickle
from flask import Flask, render_template, request
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

patterns = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone_number": r"\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b",
    "dob": r"\b(?:\d{1,2}[-/\s])?(?:\d{1,2}[-/\s])?(?:\d{2,4})\b",
    "aadhar_num": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d{4}[\s-]?){3}\d{4}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])/\d{2,4}\b",
    "full_name": r"\b([A-Z][a-z]+\s[A-Z][a-z]+)\b"
}

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def mask_text(text):
    for entity, pattern in patterns.items():
        text = re.sub(pattern, f"[{entity}]", text)
    return text

def preprocess(text):
    tokens = nltk.word_tokenize(text)
    return " ".join([
        stemmer.stem(word.lower())
        for word in tokens
        if word.isalpha() and word.lower() not in stop_words
    ])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    masked = mask_text(email_text)
    processed = preprocess(masked)
    prediction = model.predict([processed])[0]

    return render_template('index.html',
                           masked_email=masked,
                           preprocessed_email=processed,
                           prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
