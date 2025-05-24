from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary
