import streamlit as st
from core.llm_client import frage_an_llm

def zeige_chat_interface(garmin_data):
    st.subheader("🤖 Chat mit deinem Coach")
    frage = st.text_input("Was möchtest du wissen?")
    if frage:
        with st.spinner("Denke nach..."):
            antwort = frage_an_llm(frage, garmin_data)
            st.markdown("### Antwort vom LLM:")
            st.write(antwort)
