import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page title
st.title("Streaming Chatbot")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask something..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Streaming LLM response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=st.session_state.messages[-6:],  # Send last 6 messages for context
            stream=True,
            max_tokens=500
        )

        answer = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in stream
            if chunk.choices[0].delta.content
        )

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })