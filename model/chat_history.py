import os

CHAT_HISTORY_FILE = "chat_history.txt"

def save_chat(user_input, bushra_response):
    with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"User: {user_input}\n")
        f.write(f"Bushra: {bushra_response}\n\n")

def load_chat_history():
    if not os.path.exists(CHAT_HISTORY_FILE):
        return ""
    with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
        return f.read()
