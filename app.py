import streamlit as st

from utils.ner import extract_named_entities
from utils.sentiment import analyze_sentiment
from utils.classifier import classify_text
from utils.summarizer import summarize_text
from utils.keywords import extract_keywords
from utils.language import detect_language

st.set_page_config(page_title="Smart NLP Analyzer", layout="wide")

st.title("🧠 Smart NLP Analyzer")
st.markdown("Analyze your text using multiple Natural Language Processing tools in one place.")

text = st.text_area("✍️ Enter Text to Analyze", height=200)

if st.button("🔍 Analyze") and text:
    with st.spinner("Running NLP tools..."):

        # Named Entity Recognition
        st.subheader("🔍 Named Entity Recognition (NER)")
        entities = extract_named_entities(text)
        if entities:
            for ent, label in entities:
                st.markdown(f"**{ent}** → `{label}`")
        else:
            st.info("No named entities found.")

        # Sentiment Analysis
        st.subheader("😊 Sentiment Analysis")
        sentiment = analyze_sentiment(text)
        st.json(sentiment)

        # Text Classification
        st.subheader("🏷️ Zero-Shot Text Classification")
        labels = ["business", "sports", "politics", "education", "entertainment"]
        classification = classify_text(text, labels)
        st.json(classification)

        # Summarization
        st.subheader("🧾 Text Summarization")
        summary = summarize_text(text)
        st.write(summary[0]['summary_text'])

        # Keyword Extraction
        st.subheader("🔑 Keyword Extraction")
        keywords = extract_keywords(text)
        st.write(", ".join(keywords))

        # Language Detection
        st.subheader("🌐 Language Detection")
        lang = detect_language(text)
        st.write(f"Detected Language: `{lang}`")
