import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool 🌐")

text = st.text_area("Enter your text here:", "Hello, how are you?")

langs = {
    'English': 'en',
    'Arabic': 'ar',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Chinese': 'zh-CN',
    'Hindi': 'hi',
    'Russian': 'ru'
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select source language:", list(langs.keys()), index=0)
with col2:
    target_lang = st.selectbox("Select target language:", list(langs.keys()), index=1)

if st.button("Translate"):
    try:
        translated = GoogleTranslator(
            source=langs[source_lang], target=langs[target_lang]
        ).translate(text)
        st.success(f"**Translated text:**\n{translated}")
    except Exception as e:
        st.error(f"An error occurred during translation: {e}")
