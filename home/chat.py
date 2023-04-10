# Import the necessary libraries
import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hi there!", "Hello!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you.", "I'm good, thanks for asking!"]),
    (r"what is your name?", ["My name is Chatbot.", "I'm Chatbot, nice to meet you."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!"]),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello, I'm Chatbot! How can I help you today?")
chatbot.converse()
