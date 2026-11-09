import os
import time
from google import genai

# Initialize the Gemini client 
client = genai.Client()

# Use the current active model
chat = client.chats.create(model="gemini-3.8-flash")

print("==================================================")
print("  🤖 Google Gemini AI Chatbot Initialized!")
print("  Type 'quit' or 'exit' to end the session.")
print("==================================================\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower().strip() in ["quit", "exit"]:
        print("\nSession ended. Goodbye!")
        break
    
    if not user_input.strip():
        continue

    # Automatic retry loop for temporary server traffic (503 errors)
    max_retries = 3
    success = False
    
    for attempt in range(max_retries):
        try:
            response = chat.send_message(user_input)
            print(f"\nAI: {response.text}\n")
            success = True
            break
        except Exception as e:
            # Check if it's a high demand/unavailable error and we have retries left
            if ("503" in str(e) or "UNAVAILABLE" in str(e)) and attempt < max_retries - 1:
                print(f"\n[Servers busy, retrying automatically... (Attempt {attempt + 1})]")
                time.sleep(2) # Wait 2 seconds before trying again
            else:
                print(f"\nAn error occurred: {e}\n")
                break