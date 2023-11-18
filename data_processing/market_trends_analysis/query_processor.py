# query_processor.py
import spacy

nlp = spacy.load("en_core_web_sm")

def process_query(query):
    doc = nlp(query)
    topics = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return topics
