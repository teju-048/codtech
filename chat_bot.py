import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good.\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!", "It was nice talking to you. Bye!"]
    ],
    [
        r"(.*)",
        ["I didn't get that. Can you say it differently?"]
    ],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
chatbot.converse()
