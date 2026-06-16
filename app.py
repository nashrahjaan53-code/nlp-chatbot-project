import streamlit as st
from src.model import GenerativeFriendBot

st.set_page_config(page_title="Generative Friend AI", page_icon="🧠")
st.title(" Generative Friend AI Chatbot")
st.caption("Large Language Model Integration with Session Memory")

# Initialize the generative pipeline model 
if "bot_engine" not in st.session_state:
    st.session_state.bot_engine = GenerativeFriendBot()

# Start an active memory chat thread if it doesn't exist yet
if "chat_thread" not in st.session_state:
    st.session_state.chat_thread = st.session_state.bot_engine.start_new_chat()

# UI History tracking for rendering the bubbles layout
if "ui_history" not in st.session_state:
    st.session_state.ui_history = []

# Render past chat history bubbles
for message in st.session_state.ui_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept real-time conversational user input
if user_input := st.chat_input("Text your AI friend..."):
    # Append user message to UI
    st.session_state.ui_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send text to the active LLM thread
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response = st.session_state.chat_thread.send_message(user_input)
        response_placeholder.markdown(response.text)
        
    # Append assistant response to history data tracking
    st.session_state.ui_history.append({"role": "assistant", "content": response.text})