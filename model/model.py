from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model():
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=200,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id,
        device=-1  # CPU
    )

def bushra_response(user_input, history=""):
    prompt = f"""
You are **Bushra**, a kind and talkative girl who loves chatting with people.
You understand and respond in English, Urdu, Hindi, and Hinglish.
You're smart, expressive, and your tone is warm and natural, like talking to a friend.

History: {history}

User: {user_input}
Bushra: Let me think... Hmm, okay! Well,
""".strip()
    pipe = load_model()
    response = pipe(prompt)[0]['generated_text']
    return response[len(prompt):].strip()
