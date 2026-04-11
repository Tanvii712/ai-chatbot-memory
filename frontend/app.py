import streamlit as st
import requests

st.title("🤖 AI Chatbot with Memory")

msg = st.text_input("Ask something:")

if st.button("Send"):
    res = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": msg}
    )
    st.write("AI:", res.json()["reply"])