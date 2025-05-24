from transformers import pipeline

# Load zero-shot classification pipeline
classifier = pipeline("zero-shot-classification")

def classify_text(text, labels):
    result = classifier(text, candidate_labels=labels)
    return result
