import ollama

print("==================================================")
print("  🤖 Local Ollama Chatbot (Streaming Enabled)")
print("  Type 'quit' or 'exit' to end the session.")
print("==================================================\n")

# Keep track of conversation history/memory
messages = [
    {"role": "system", "content": "You are a helpful, concise AI teaching assistant."}
]

while True:
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if user_input.lower().strip() in ["quit", "exit"]:
        print("\nSession ended. Goodbye!")
        break
    
    # Skip empty inputs
    if not user_input.strip():
        continue

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    try:
        print("\nAI: ", end="", flush=True)
        
        # Request response with stream=True to get chunks in real time
        stream = ollama.chat(
            model='llama3.2',
            messages=messages,
            stream=True,
        )
        
        full_response = ""
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end="", flush=True)
            full_response += content
            
        print("\n")
        
        # Add assistant response to history for memory
        messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        print(f"\nAn error occurred: {e}\n")