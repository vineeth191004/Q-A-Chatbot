from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Match variable in .env

# Initialize Gemini Model
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit UI
st.set_page_config(page_title="Q&A Demo")
st.markdown(
    """
    <style>
    /* Background with gradient */
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        font-family: 'Arial', sans-serif;
    }

    /* Input and button styling */
    .stTextInput input {
        background-color: #ffffff;
        color: #000;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton button {
        background-color: #ff7f50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 8px 16px;
    }
    .stButton button:hover {
        background-color: #ff4500;
    }

    /* Chat history styling */
    .chat-history {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
        margin-top: 15px;
    }

    h1, h2, h3, h4 {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("💬 Gemini LLM Application")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("The Chat History is")
with st.container():
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    for role, text in st.session_state['chat_history']:
        st.write(f"**{role}:** {text}")
    st.markdown('</div>', unsafe_allow_html=True)
