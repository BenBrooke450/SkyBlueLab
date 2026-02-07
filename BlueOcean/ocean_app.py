
import ollama

def run_ocean():

    # Choose your model: 'ministral-3:3b' or 'ministral-3:8b'
    model_name = 'ministral-3:3b'

    messages = [
        {'role': 'system', 'content': 'You are a helpful AI assistant powered by Ministral.'}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit']:
            break

        messages.append({'role': 'user', 'content': user_input})

        response = ollama.chat(model=model_name, messages=messages)

        bot_reply = response['message']['content']
        print(f"\nMinistral: {bot_reply}\n")
        messages.append({'role': 'assistant', 'content': bot_reply})