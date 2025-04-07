import streamlit as st
import requests
import base64

st.title("🔊 ElevenLabs Text-to-Speech Tool")

# Input your ElevenLabs API Key
API_KEY = st.text_input("sk_20b1a5899d669aed061c48e8242efd55f43abf2445bfd0f3", type="password")

# Input text for speech synthesis
text = st.text_area("Enter text to convert to speech:")

# Choose voice (these are public demo voices from ElevenLabs)
voices = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Domi": "AZnzlk1XvdvUeBnXmlld",
    "Bella": "EXAVITQu4vr4xnSDxMaL"
    "Liam": "TX3LPaxmHKxFdv7VOQHJ"
}
selected_voice = st.selectbox("Choose a Voice", list(voices.keys()))
voice_id = voices[selected_voice]

if st.button("🔈 Generate Speech") and API_KEY and text:
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",  # You can use other model IDs if needed
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            audio_data = response.content
            b64_audio = base64.b64encode(audio_data).decode()

            st.audio(audio_data, format='audio/mp3')
            st.success("Speech generated successfully!")

            # Option to download
            st.download_button("⬇️ Download Audio", data=audio_data, file_name="speech.mp3")
        else:
            st.error(f"Failed to generate speech: {response.text}")

    except Exception as e:
        st.error(f"Error: {e}")
