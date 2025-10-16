import streamlit as st
import requests
import base64

# ===============================
# 🌈 Custom CSS Styling
# ===============================
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #00bcd4, #4caf50);
        padding: 50px 0;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        font-size: 3em;
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }

    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #ffffff;
        border: 2px solid #00bcd4;
        padding: 12px;
        border-radius: 12px;
        font-size: 1.1em;
        transition: border-color 0.3s ease;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > textarea:focus {
        border-color: #4caf50;
    }

    .stButton > button,
    .stDownloadButton > button {
        background-color: #00bcd4;
        color: white;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 1.2em;
        transition: background-color 0.3s ease;
        border: none;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background-color: #4caf50;
    }

    .stSelectbox > div {
        background-color: #ffffff;
        border-radius: 12px;
        border: 2px solid #00bcd4;
        padding: 12px;
        transition: border-color 0.3s ease;
    }

    .stSelectbox > div:focus-within {
        border-color: #4caf50;
    }

    .stAudio {
        margin-top: 20px;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
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


# ===============================
# 🎙️ APP TITLE
# ===============================
st.title("🔊 JunaidYT AI33.pro Text-to-Speech Tool")


# ===============================
# 🔑 API Key Input
# ===============================
API_KEY = st.text_input("Enter your AI33.pro API Key", type="password").strip()


# ===============================
# 📝 Text Input
# ===============================
text = st.text_area("Enter text to convert to speech:")


# ===============================
# 🗣️ Voice Selection with IDs
# ===============================
voices = {
    "knox dark 2": "dPah2VEoifKnZT37774q",
    "Junaid": "abc123xyz",
    "Male": "male",
    "Female": "female"
}

selected_voice = st.selectbox("Choose a Voice", list(voices.keys()))
voice_id = voices[selected_voice]


# ===============================
# ⚡ Speed Control
# ===============================
speed = st.slider("Select Speech Speed", min_value=0.5, max_value=2.0, value=1.0, step=0.1)


# ===============================
# 🎧 Generate Speech
# ===============================
if st.button("🎤 Generate Speech"):
    if not text:
        st.warning("⚠️ Please enter some text to convert.")
    else:
        try:
            url = "https://ai33.pro/app/api-document"  # Replace with the correct API endpoint if needed
            headers = {
                "Content-Type": "application/json"
            }
            if API_KEY:
                headers["Authorization"] = f"Bearer {API_KEY}"

            payload = {
                "text": text,
                "voice": voice_id,
                "speed": speed
            }

            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                audio_data = response.content
                st.audio(audio_data, format="audio/mp3")
                st.success("✅ Speech generated successfully!")
                st.download_button(
                    label="⬇️ Download Audio",
                    data=audio_data,
                    file_name="speech_ai33.mp3",
                    mime="audio/mp3"
                )
            else:
                st.error(f"❌ Failed to generate speech:\n{response.text}")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
