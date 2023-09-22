import requests


class TgUnit:

    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def replace_digits_with_emojis(self, input_string):
        emoji_digits = {
            "0": "0️⃣",
            "1": "1️⃣",
            "2": "2️⃣",
            "3": "3️⃣",
            "4": "4️⃣",
            "5": "5️⃣",
            "6": "6️⃣",
            "7": "7️⃣",
            "8": "8️⃣",
            "9": "9️⃣",
        }

        result = ""
        for char in input_string:
            if char.isdigit():
                result += emoji_digits[char]
            else:
                result += char
        return result

    def send_message(self, message):
        method = 'sendMessage'
        url = f"https://api.telegram.org/bot{self.token}/{method}" + "?chat_id=" + self.chat_id + "&text=" + message + "&parse_mode=HTML"
        response = requests.get(url)
        return response

