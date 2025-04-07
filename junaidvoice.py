import streamlit as st
import requests
import base64

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }

    h1 {
        font-size: 3em;
        color: #2c3e50;
        font-weight: bold;
        text-align: center;
    }

    .stTextInput > div > div > input {
        background-color: #ffffff;
        border: 2px solid #6c757d;
        padding: 10px;
        border-radius: 10px;
    }

    .stTextArea > div > textarea {
        background-color: #ffffff;
        border: 2px solid #6c757d;
        padding: 10px;
        border-radius: 10px;
    }

    .stButton > button {
        background-color: #2c3e50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 1.1em;
    }

    .stSelectbox > div {
        background-color: #ffffff;
        border-radius: 10px;
        border: 2px solid #6c757d;
        padding: 5px;
    }

    .stAudio {
        margin-top: 20px;
    }

    .stDownloadButton > button {
        background-color: #27ae60;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 1em;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🔊 JunaidYT Text-to-Speech Tool")

# Input your ElevenLabs API Key
API_KEY = st.text_input("Enter Passwords", type="password")

# Input text for speech synthesis
text = st.text_area("Enter text to convert to speech:")

# Voice selection
voices = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Domi": "AZnzlk1XvdvUeBnXmlld",
    "Bella": "EXAVITQu4vr4xnSDxMaL",
    "Liam": "TX3LPaxmHKxFdv7VOQHJ",
    "Knox Dark 2": "dPah2VEoifKnZT37774q",
    "Jeremy (Legacy)": "bVMeCyTHy58xNoL34h3p",
    "Adam (legacy)": "N2lVS1w4EtoT3dr4eOWO",
    "Callum ": "X1tufN2s4pZ5Z7j8p23n"
}

selected_voice = st.selectbox("Choose a Voice", list(voices.keys()))
voice_id = voices[selected_voice]

# Speed selection (rate)
rate = st.slider("Select Speech Speed", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

if st.button("🔈 Generate Speech") and API_KEY and text:
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5,
                "rate": rate  # Adding the rate parameter to adjust speed
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            audio_data = response.content
            b64_audio = base64.b64encode(audio_data).decode()

            st.audio(audio_data, format='audio/mp3')
            st.success("Speech generated successfully!")

            st.download_button("⬇️ Download Audio", data=audio_data, file_name="speech.mp3")
        else:
            st.error(f"Failed to generate speech: {response.text}")

    except Exception as e:
        st.error(f"Error: {e}")
