import random


def generate():
    random_list = ["Please try writing something more descriptive.",
                   "Oh! It appears you wrote something I don't understand yet",
                   "Do you mind trying to rephrase that?",
                   "I'm terribly sorry, I didn't quite catch that.",
                   "I can't answer that yet, please try asking something else."
                   ]
    random_index = random.randrange(len(random_list))
    random_response = random_list[random_index]
    return random_response

