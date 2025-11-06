import streamlit as st
import io
from agent import get_response  # Import from your agent file
import base64
########
# --- MEMORY MANAGEMENT ---
def build_memory_prompt(new_query: str):
    """Builds a prompt with recent conversation memory."""
    sep = "\n"
    memory = st.session_state.get("memory", [])

    # Build the conversation history as a single text block
    chat_history = sep.join(memory)
    chat_template = f"Previous conversation:\n{chat_history}\n\nLatest query: {new_query}"
    return chat_template




############
# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Python Tutor 🕹️",
    layout="wide",
    initial_sidebar_state="expanded"  # 👈 This makes sidebar visible on load
)

# --- LOAD EXTERNAL CSS ---
def load_css(path: str):
    with open(path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# --- HEADER SECTION (Left Aligned Arcade Look) ---
st.markdown("""
<div class='header-container'>
    <div class='arcade-char'>👾</div>
    <div>
        <div class='header-title'>PYTHON TUTOR </div>
        <div class='header-sub'>Learn · Debug · Level Up</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PERSISTENT WELCOME MESSAGE ---
st.markdown("""
<div class='welcome-banner'>
    <h3>Welcome!</h3>
    <p>This is your Python Tutor — ask questions, run ideas, and level up your Python skills.</p>
    <p><em>Example:</em> "How does Python handle memory management?"</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR (About + Export Chat) ---
with st.sidebar:
    st.title("🕹️ ")

    st.markdown("""
    <div class='sidebar-info'>
        <h3>About</h3>
        <p><strong>Python Tutor </strong> is an interactive learning hub that helps you understand Python concepts!</p>
    </div>
    """, unsafe_allow_html=True)



# Export Chat Section
    st.markdown("<h3>💾 Export Chat</h3>", unsafe_allow_html=True)

    if st.button("Download Chat"):
        # Check if messages exist in session
        if "messages" in st.session_state and st.session_state.messages:
            # Combine all messages into a readable format
            chat_text = "\n\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.messages])
            buffer = io.BytesIO(chat_text.encode('utf-8'))
            st.download_button("📥 Save Chat", buffer, file_name="PythonTutorArcade_Chat.txt")
        else:
            st.warning("No chat history yet!")

    st.markdown("---")
    st.caption("💡 Tip: Try typing *'Explain recursion with an example.'*")


# --- Chat Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "memory" not in st.session_state:
    st.session_state.memory = []  # Stores short recent history


# --- Display Chat Messages ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input ---
if prompt := st.chat_input("Ask me anything about Python 👇"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    #with st.chat_message("assistant"):
     #   response = get_response(prompt)
      #  st.markdown(response)
    with st.chat_message("assistant"):
    # Include memory in prompt
        chat_template = build_memory_prompt(prompt)
        response = get_response(chat_template)
        st.markdown(response)

# Update memory (keep last  exchanges)
    st.session_state.memory.append(f"User: {prompt}\nAgent: {response}")
    #st.session_state.memory = st.session_state.memory[-5:]
  



    st.session_state.messages.append({"role": "assistant", "content": response})
