from transformers import pipeline

# Load Hugging Face sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result
