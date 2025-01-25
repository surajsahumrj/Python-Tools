import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

# Initialize the conversation
messages = [
    {"role": "system", "content": "You are a helpful and intelligent assistant."}
]

# Start the chat loop
while True:
    # Get user input
    message = input("You: ")
    if not message.strip():
        print("Exiting the chat. Goodbye!")
        break

    # Add user input to messages
    messages.append({"role": "user", "content": message})

    # Get the response from the ChatGPT API
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract and print the assistant's reply
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")

    # Add assistant's reply to messages
    messages.append({"role": "assistant", "content": reply})
