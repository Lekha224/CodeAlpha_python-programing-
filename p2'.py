def get_response(user_input):
    match user_input:
        case 'hi':
            return 'Hello! How can I assist you today?'
        case 'Hi':
            return 'Hello! How can I assist you today?'
        case 'hello':
            return 'Hi there! How can I help you?'
        case 'Hello':
            return 'Hi there! How can I help you?'
        case 'How are you':
            return 'I am just a computer program, but thanks for asking!'
        case 'how are you':
            return 'I am just a computer program, but thanks for asking!'
        case 'what is your name?':
            return 'I am a chatbot created by you.'
        case 'What is your name?':
            return 'I am a chatbot created by you.'
        case 'bye':
            return 'Goodbye! Have a great day!'
        case 'Bye':
            return 'Goodbye! Have a great day!'
        case 'quit':
            return 'Goodbye! Have a great day!'
        case 'Quit':
            return 'Goodbye! Have a great day!'
        case _:
            return "Sorry, I didn't understand that."

def chat():
    print("Hello! I am a basic chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        if user_input in ['quit', 'Quit', 'bye', 'Bye']:
            break

if __name__ == "__main__":
    chat()

