import os
from openai import OpenAI

# Initialize client using the environment variable
client = OpenAI()

# Set initial system instructions and memory list
messages = [
    {"role": "system", "content": "You are a helpful, concise AI teaching assistant."}
]

print("==================================================")
print("  AI Chatbot Initialized!")
print("  Type 'quit' or 'exit' to end the session.")
print("==================================================\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower().strip() in ["quit", "exit"]:
        print("\nSession ended. Goodbye!")
        break
    
    if not user_input.strip():
        continue

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        
        bot_reply = response.choices[0].message.content
        print(f"\nAI: {bot_reply}\n")
        
        messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print(f"\nError: {e}\n")