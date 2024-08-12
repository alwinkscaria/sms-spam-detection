from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize Flask app
app = Flask(__name__)

# Load the Logistic Regression model and TFIDFVectorizer
with open('models/logistic_regression_model.pkl', 'rb') as model_file:
    model_lr = pickle.load(model_file)

with open('models/tfidf_vectorizer.pkl', 'rb') as vect_file:
    vect = pickle.load(vect_file)

# Text preprocessing functions...

def preprocess_text(text):
    # Preprocessing steps: cleaning, removing stopwords, stemming
    return text

def predict_spam(text):
    processed_text = preprocess_text(text)
    vectorized_text = vect.transform([processed_text])
    prediction = model_lr.predict(vectorized_text)
    return "spam" if prediction[0] == 1 else "not spam"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    prediction = predict_spam(text)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
