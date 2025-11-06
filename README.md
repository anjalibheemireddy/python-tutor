# python-tutor
An interactive AI-powered learning assistant built with Streamlit that helps users master Python through guided explanations, examples, and practice conversations.
The system uses a conversational interface to provide contextual tutoring on Python concepts, enabling learners to understand code step-by-step

## Prerequisites
- Python 3.10 or higher
- pip for dependency management
- GROQ api key.

## Installation
1. ```bash git clone https://github.com/anjalibheemireddy/python-tutor.git  cd python-tutor```
2. You can use venv or conda:
  ```bash python -m venv venv ```
   Activate it:
```bash venv\Scripts\activate```
   On macOS/Linux
```bash source venv/bin/activate```
3. Create a `.env` file in the project root with your API keys:
```bash GROQ_API_KEY=your_groq_key```
5. Run the app locally:
```bash streamlit run app.py ```

Interactive Python tutoring via a conversational interface

Context-aware explanations for beginner to intermediate topics

Retro arcade-style Streamlit UI for an engaging experience

Dynamic hints and examples for coding exercises

Persistent chat view that retains session history (optional)

Customizable agent logic via agent.py





