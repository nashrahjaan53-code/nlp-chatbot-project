import streamlit as st
import os
from dotenv import load_dotenv

# 1. Load the local hidden .env file right when the app boots up
load_dotenv()

# 2. Import your generative model engine
from src.model import GenerativeFriendBot

# 3. Configure the web application layout and headers
st.set_page_config(page_title="Generative Friend AI", page_icon="🧠")
st.title(" Generative Friend AI Chatbot")
st.caption("Data Science Portfolio: Large Language Model Integration with Session Memory")

# Initialize the generative pipeline model and store it in session state
if "bot_engine" not in st.session_state:
    st.session_state.bot_engine = GenerativeFriendBot()

# Start an active conversational memory thread if it doesn't exist yet
if "chat_thread" not in st.session_state:
    st.session_state.chat_thread = st.session_state.bot_engine.start_new_chat()

# UI History tracking for rendering the message bubbles layout
if "ui_history" not in st.session_state:
    st.session_state.ui_history = []

# Render all past chat history bubbles from the current session
for message in st.session_state.ui_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept real-time conversational input from the user
if user_input := st.chat_input("Text your AI friend..."):
    # Append user message to the visual UI history array
    st.session_state.ui_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send the raw text to the active LLM thread session
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # The model automatically processes conversation context natively
        response = st.session_state.chat_thread.send_message(user_input)
        # Stream the markdown response cleanly into the placeholder
        response_placeholder.markdown(response.text)
        
    # Append the assistant's generated response to the UI history array
    st.session_state.ui_history.append({"role": "assistant", "content": response.text})