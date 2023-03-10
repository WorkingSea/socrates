#!/usr/bin/env python3
import random

replacement = {
    "me": "you",
    "you": "me, socrates,",
    "ya": "me, socrates,", 
    "i am": "you are",
    "i": "you",
    "my": "your",
    "mine": "yours",
    "yours": "mine",
    "your": "my",
    "am": "are",
    "are": "am",
    "you're": "i am",
    "you've": "i have",
    "we": "you",
    "i'm": "you're",
    "i've": "you have",
    "you'll": "i'll",
    "i'll": "you'll",
    "because": "",
    "'cause": "",
}


answers = [
    # Answers that ignore user input
    "tell me more about it",
    "please elaborate",
    # Answers that utilize user input
    "how do you know that",
    "why is it so that",
    "what makes it so that",
    "why do you think that",
]

exit_strings = [
    "bye",
    "goodbye",
    "see you later",
    "i need to go",
    "cya",
]


def Answer(message):
    for keyword in exit_strings:
        if keyword in message:
            print("Socrates: goodbye")
            exit()
    words = message.split()
    replaced_words = [
        word if word not in replacement else replacement[word] for word in words
    ]
    random_number = random.randint(0, (len(answers) - 1))
    if random_number < 2:  # 2 is the numbers we have that don't use the user input
        return answers[random_number]
    else:
        reply = []
        reply.append(answers[random_number])
        reply.extend(replaced_words)
        reply = " ".join(reply).replace("  ", " ")
        return reply


def Main():
    message = input("You: ")
    reply = "Socrates: " + Answer(message.lower()) + "?"
    print(reply)
    Main()


print("Socrates: what's your belief?")
Main()
