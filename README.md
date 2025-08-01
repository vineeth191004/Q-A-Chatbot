# 💬 Gemini LLM Application

This project is a **Streamlit-based web application** that integrates with **Google's Gemini (Generative AI)** to provide an interactive Q\&A chatbot. Users can input questions, and the Gemini LLM responds with relevant answers in real time. The app includes a custom-styled UI with a gradient background and chat history display.

---

## 🚀 Features

* 🌐 **Interactive UI** built with Streamlit
* 🤖 **Google Gemini LLM** integration for Q\&A
* 🎨 Custom CSS styling (gradient background, styled buttons, and chat history)
* 💬 Persistent chat history within the session
* 🔑 Secure API key handling with `.env` for deployment

---

## 🛠️ Technologies Used

* **Python 3.9+**
* **Streamlit** (for UI development)
* **Google Generative AI SDK** (`google-generativeai`)
* **dotenv** (for local environment variable management)
* **HTML/CSS** (for custom UI styling)

---

## 📂 Project Structure

```
gemini-llm-app/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (local only)
└── README.md             # Project documentation
```

---

## ⚙️ Installation and Setup

### 1️ Clone the Repository

```bash
git clone https://github.com/vineeth191004/Q-A-Chatbot.git

```

### 2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3 Add API Key

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## ▶️ Run the Application

```bash
streamlit run qachat.py
```

Open the link shown in the terminal (e.g. `http://localhost:8501`) in your browser.

---

## 🌐 Deployment

You can deploy this app easily using **[Streamlit Community Cloud](https://share.streamlit.io/)**:

1. Push the project to GitHub.
2. Connect GitHub repo in Streamlit Cloud.
3. Add your API key.
4. Deploy!

---

Would you like me to also give you a **`requirements.txt`** file for this app (ready for deployment)? (so it works perfectly on Streamlit Cloud)
