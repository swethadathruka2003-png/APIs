import streamlit as st
from openai import OpenAI

st.title("My AI Chatbot")

api_key = st.text_input("Enter API Key", type="password")

question = st.text_input("Ask something:")

if st.button("Send"):
    if not api_key:
        st.error("Please enter your API key")
    elif not question:
        st.warning("Please enter a question")
    else:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5.6",
            input=question
        )

        st.write(response.output_text)