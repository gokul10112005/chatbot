# chatbot.py
# Simple keyword-based chatbot

# Predefined responses
responses = {
    "greeting": ["Hello! How are you?", "Hi there! Nice to meet you!", "Hey! How's your day?"],
    "name": ["I am Chatty, your friendly chatbot!", "My name is Chatty."],
    "how are you": ["I'm just a bot, but I'm doing great!", "Feeling awesome, thanks for asking!"],
    "bye": ["Goodbye! Have a nice day!", "See you later! Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"]
}

# Function to find the right response


def get_response(user_input):
    user_input = user_input.lower()

    # Keyword matching
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return responses["greeting"][0]
    elif "your name" in user_input:
        return responses["name"][0]
    elif "how are you" in user_input:
        return responses["how are you"][0]
    elif "bye" in user_input or "exit" in user_input:
        return responses["bye"][0]
    elif "thank" in user_input:
        return responses["thanks"][0]
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# Main chat loop


def chat():
    print("Chatbot: Hi! I am Chatty. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break


# Run the chatbot
if __name__ == "__main__":
    chat()
