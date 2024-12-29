import spacy
import numpy as np

# Define your sentences
sentences = ["I am a student", "This is a test sentence", "Another example sentence"]

# Load the spaCy model
nlp = spacy.load('en_core_web_md')

# Get the number of sentences and the embedding dimension
n_sentence = len(sentences)
embedding_dim = nlp.vocab.vectors_length

# Initialize a numpy array to hold the sentence vectors
x = np.zeros((n_sentence, embedding_dim))

# Process each sentence and store its vector
for idx, sentence in enumerate(sentences):
    doc = nlp(sentence)
    x[idx, :] = doc.vector

# Example sentence
sentence = "I am a student"