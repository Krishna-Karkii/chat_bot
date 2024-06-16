import re
import json
import random_response


with open("bot_data.json") as file:
    contents = json.load(file)


class ChatBot:
    def __init__(self, user_prompt):
        self.user_prompt = user_prompt

    def get_data(self):
        split_message = re.split(r'\s+|[,;?!.-]\s*', self.user_prompt.lower())
        score_list = []

        for content in contents:
            response_score = 0
            required_score = 0
            required_words = content['required_words']

            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            if required_score == len(required_words):
                for word in split_message:
                    if word in content['user_input']:
                        response_score += 1

            score_list.append(response_score)

        if self.user_prompt == "":
            return random_response.generate()

        max_num = max(score_list)
        response_index = score_list.index(max_num)

        if max_num != 0:
            response_message = contents[response_index]['bot_response']
            return response_message

        return random_response.generate()


if __name__ == "__main__":
    while True:
        user_prompt = input("Enter a message: ")
        chat_bot = ChatBot(user_prompt)
        response = chat_bot.get_data()
        print(response)


