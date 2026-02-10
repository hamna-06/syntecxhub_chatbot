import logging

logging.basicConfig(
    filename="chatbot_history.log",
    level=logging.INFO,
    format="%(asctime)s — USER: %(message)s"
)

def log_interaction(user, bot):
    logging.info(f"{user} ||| BOT: {bot}")
