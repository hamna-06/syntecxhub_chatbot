from chatbot import AdvancedChatbot
from logger import log_interaction

bot = AdvancedChatbot()
print("Chatbot started! (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "bye", "quit"]:
        response = "Thanks for chatting! Goodbye."
        print("Bot:", response)
        log_interaction(user_input, response)
        break

    response = bot.respond(user_input)

    print("Bot:", response)
    log_interaction(user_input, response)
