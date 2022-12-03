'''
Домашняя работа №6

Тут все довольно просто - добавьте новые знания, о лямбдах и новых типах аргументах + тайпинге к текущему коду.

Кроме основного задания я еще добавил декоратор, чтоб выяснит для себя и этот момент в функциональном программировании.
Сделал декоратор пока без использования @wraps() модуля functools, для точного понимания как именно работает декоратор.
Прошу проверить правильность реализации декоратора и подсказать, целесообразно ли в этом коде использовать такой декоратор.
'''


word: str = input('Enter the word ("hello" for exempl): ') # "hello"

user: dict = {
    "name": "Andrii",
    "level": 1
}

message: dict = {
    'user': user,
    'word': word,
}

sentences: list = [
    {"level": 1, "text": "Hello, my dear friend!"},
    {"level": 1, "text": "Hi Tom, I'm Andrii."},
    {"level": 2, "text": "Cheerleading hello cheers can be used in a variety of ways."},
    {"level": 1, "text": "Darkyn didn't tear the fabric between worlds for a simple hello."},
    {"level": 3, "text": "Why don't we leave it at that?"},
    {"level": 4, "text": "English lessons is fun because we get knowledge"}
]


class Traslator():

    def decorator_function(wrapped_func: list) -> str:
        def wrapper(*args, **kwargs):
            result = wrapped_func(*args, **kwargs)
            result_message = ""
            
            if len(result) > 1:
                for item in result:
                    result_message += item + "\n...\n"
            else:
                result_message += str(result)

            return str(result_message)

        return wrapper

    @decorator_function
    @staticmethod 
    def find_matched_sentences(self, user: dict, message: dict, sentences: list) -> tuple:
        result :list = []

        for sentence in sentences:
            if user["level"] == sentence["level"]:
                if message.get("word").lower() in sentence.get("text").lower():
                    result.append(sentence.get("text"))
        if not result:
            result.append("The word is not found or your level is not enough for search sentences via this word")

        return result


translator = Traslator()
# print(translator.find_matched_sentences(user, message, sentences))
