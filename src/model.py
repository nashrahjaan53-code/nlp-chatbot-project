import os
from google import genai
from google.genai import types

class GenerativeFriendBot:
    def __init__(self):
        # Clean production setup: No hardcoded keys. 
        # GenAI automatically checks os.environ["GEMINI_API_KEY"] natively.
        self.client = genai.Client()
        self.model_name = "gemini-2.5-flash"
        
        self.system_instruction = (
            "You are a close, casual human friend. Talk naturally using informal language, slang, "
            "and humor. Never repeat yourself robotically. Keep responses brief, engaging, and friendly, "
            "just like a real buddy texting back and forth. You have complete memory of this chat history."
        )

    def start_new_chat(self):
        config = types.GenerateContentConfig(
            system_instruction=self.system_instruction,
            temperature=0.7,
        )
        return self.client.chats.create(model=self.model_name, config=config)