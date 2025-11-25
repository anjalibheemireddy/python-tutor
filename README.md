## 🕹️ Python Tutor 
– Interactive AI-Powered Python Learning Bot

Python Tutor is an AI-driven teaching assistant built with Groq LLaMA-3.1, Streamlit, and a custom memory layer.
It helps users learn Python with clear explanations, examples, and debugging guidance — all wrapped in a retro arcade-styled UI.

## 🚀 Features
### ✅ AI Tutor Powered by Groq

Uses LLaMA-3.1-8B-Instant via Groq API

Structured system prompt ensures the bot behaves like a patient Python instructor

### 🧠 Conversation Memory

Lightweight memory stored in st.session_state.memory

Persists a limited amount of recent exchanges

Injected into prompt with build_memory_prompt()

🔄 Streaming Responses

Uses Groq’s streaming completion for real-time output

## 📁 Project Structure
project/
│── agent.py            # Groq client + core response generator
│── app3.py             # Streamlit UI with memory and chat rendering
│── chatmanager.py      # Terminal-based chatting
│── style.css           # Arcade-style UI theme
│── README.md           # (You are here)
│── .env                # Store your GROQ_API_KEY

## ⚙️ Installation & Setup
1.  Clone the Project
```bash
git clone <your-repo-url>
cd python-tutor
```

2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

3. Install Dependencies
```bash
pip install streamlit groq python-dotenv
```

4. Add Your API Key

Create a file named .env:
```bash
GROQ_API_KEY=your_key_here
```

### ▶️ Running the App
Start the Streamlit Web App
```bash
streamlit run app3.py
```

The UI opens in the local browser.


## 📤 Chat Export Feature

Users can export the chat from the sidebar:

st.download_button("📥 Save Chat", ...)


This generates a .txt file with all chat messages.

🧪 Example Queries to Try

“Explain recursion with a simple example.”

“How does Python handle dictionaries internally?”

## 💡 Future Enhancements

Long-term vector memory

User accounts + saved learning sessions

Code execution sandbox

Additional AI models

Quizzes + adaptive curriculum

## 📜 License

This project is licensed under the terms included in the LICENSE file.


## Author

**Anjali Bheemireddy**  
(anjalinature156@gmail.com)

