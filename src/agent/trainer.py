import spacy
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
import joblib

nlp = spacy.load('en_core_web_sm')

file_path = "data/binary_class_sentences.csv"
df = pd.read_csv(file_path, header=None, names=['Text', 'Label'])
df['Label'] = df['Label'].astype(int)

texts = df['Text'].tolist()
labels = df['Label'].tolist()

class TfidfWeightedVectors(TransformerMixin):
    def fit(self, X, y=None):
        # Initialize and fit the TfidfVectorizer
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(X)
        self.max_idf = max(self.vectorizer.idf_)  # To use as default value
        return self

    def transform(self, X):
        # Transform the texts to a list of word vectors weighted by IDF
        return [self.tfidf_weighted_vector(text) for text in X]

    def tfidf_weighted_vector(self, text):
        doc = nlp(text)
        vectors = [self.word_vector(word) for word in doc]
        return np.mean(vectors, axis=0) if vectors else np.zeros((len(doc[0].vector),))

    def word_vector(self, word):
        # Retrieve the word's TF-IDF score and multiply it with the word vector
        vector = word.vector
        idf_score = self.vectorizer.idf_.get(word.text, self.max_idf)
        return vector * idf_score

class LinguisticFeatureTransformer(TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, texts):
        return [self.extract_linguistic_features(text) for text in texts]

    def extract_linguistic_features(self, text):
        doc = nlp(text)
        return {
            'word_count': len(doc),
            'sentence_count': len(list(doc.sents)),
            'avg_word_length': np.mean([len(token) for token in doc]),
            'noun_count': len([token for token in doc if token.pos_ == 'NOUN']),
        }

model = joblib.load('src/agent/model/spacy_model.pkl')
# Create a pipeline
pipeline = Pipeline([
    ('features', FeatureUnion([
        ('tfidf_vectors', TfidfWeightedVectors()),
        ('linguistic', LinguisticFeatureTransformer())
    ])),
    ('scaler', StandardScaler()),
    ('classifier', model)
])
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, shuffle=True)

pipeline.fit(texts, labels)