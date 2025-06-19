import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

# Import from model
import os
import sys

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now you can import from model/
from model.model import bushra_response
from model.chat_history import load_chat_history, save_chat
# Page config
st.set_page_config(page_title="👩‍🦰 Bushra - Your Talking Pal", layout="centered")
st.title("👩‍🦰 Bushra - Your Talking Pal")
st.markdown("Say anything in **English, Urdu, Hindi, or Hinglish** — I'll reply warmly!")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = load_chat_history()

user_input = st.text_input("You:", placeholder="Type or say something...")

if st.button("Talk"):
    if user_input.strip() == "":
        st.warning("Please type something.")
    else:
        with st.spinner("Thinking..."):
            response = bushra_response(user_input, st.session_state.chat_history)
        st.markdown(f"**Bushra:** {response}")

        # Save to session and file
        st.session_state.chat_history += f"\nUser: {user_input}\nBushra: {response}"
        save_chat(user_input, response)

        # Text-to-Speech
               # Text-to-Speech with safety check
        if response.strip():  # Only try TTS if there's actual text
            try:
                tts = gTTS(text=response, lang='en', tld='co.in')
                fp = BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                st.audio(fp, format="audio/mp3")
            except Exception as e:
                st.warning("Could not generate audio. Response was too short or empty.")
        else:
            st.warning("No response to speak.")
