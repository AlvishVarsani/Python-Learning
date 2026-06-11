from chat_service import ChatService

chatbot=ChatService()

print("="*50)
print("Welcome to the Java Mentor Chatbot! Ask your Java-related questions below.")
print("Type 'exit' or 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chatbot.ask_question(user_input)
    print(f"Mentor: {response}")