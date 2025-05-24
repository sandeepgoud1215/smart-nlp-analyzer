import streamlit as st
from classifier import classify_text
from keywords import extract_keywords
from ner import extract_entities
from sentiment import analyze_sentiment
from language import detect_language
from summarizer import summarize_text

st.title("Smart NLP Analyzer")

text = st.text_area("Enter text to analyze:")

if text:
    st.subheader("Language Detection")
    lang = detect_language(text)
    st.write(lang)

    st.subheader("Text Classification")
    classification = classify_text(text)
    st.write(classification)

    st.subheader("Keyword Extraction")
    keywords = extract_keywords(text)
    st.write(keywords)

    st.subheader("Named Entity Recognition")
    entities = extract_entities(text)
    st.write(entities)

    st.subheader("Sentiment Analysis")
    sentiment = analyze_sentiment(text)
    st.write(sentiment)

    st.subheader("Summarization")
    summary = summarize_text(text)
    st.write(summary)
