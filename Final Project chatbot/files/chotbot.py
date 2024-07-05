import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files
nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name ?",
        ["My name is ChatBot and I'm here to help you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Delhi',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot here in %1","Too cold here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, I have heard about it.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in %2","It's raining heavily in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy.",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi, I'm the chatbot you built\nPlease type 'quit' to exit")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
