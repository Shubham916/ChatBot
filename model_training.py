from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np
from text_processing import preprocess_text

# Sample training data
training_data = [
    ("Hello, how can I help you?", "greeting"),
    ("Goodbye", "farewell"),
    ("What is your name?", "name_query"),
    # Add more training data as needed
]

texts, labels = zip(*training_data)
processed_texts = [preprocess_text(text) for text in texts]

# TF-IDF Vectorizer and Logistic Regression pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train the model
pipeline.fit(processed_texts, labels)

def predict_intent(text):
    processed_text = preprocess_text(text)
    return pipeline.predict([processed_text])[0]
