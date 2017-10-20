from abc import ABCMeta, abstractmethod
import json


class ValueBelowZeroError(Exception):
    pass

"""
Здесь применяется паттерн шаблонный метод, поскольку алгоритм получения JSON объекта имеет небольшое отличие для
шифровки и дешифровки - вычесление буквы
"""


class Algorithm(metaclass=ABCMeta):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()

    def get_json_result(self, data: bytes) -> 'JSON object':
        """
        Метод принимает JSON-объект в виде байтов, декодирует, используя кодировку 'utf-8' и извлекает входной текст из
        словаря по ключю 'text'. Далее извлекает смещение по ключю 'offset' и преобразует его число. В случа неудачи -
        перехватывает исключение ValueError и возвращает JSON-объект с пустым результатом. Аналогичный возвращаемый
        результат и в случае, если смещение < 0, но здесь возбуждается пользовательское исключение ValueBelowZeroError.
        Далее в цикле обходит все символы в переменной 'text'. Если символ буква - ищет её индекс в алфавите и в
        зависимости от регистра использует нужный вид алфавита в аргументе шаблонного метода 'calculate_letter' для
        добавления нужной буквы в строку 'result'. Если символ не буква, то он сразу добавляется в строку 'result'.
        В конце возвращает значение в виде JSON-объекта.
        """
        result = ''
        received_json_data = json.loads(data.decode('utf-8'))
        text = received_json_data['text']
        try:
            offset = int(received_json_data['offset'])
            if offset < 0:
                raise ValueBelowZeroError
        except ValueError:
            return json.dumps({'result': result})
        except ValueBelowZeroError:
            return json.dumps({'result': result})
        for later in text:
            if later.isalpha():
                index = Algorithm.alphabet_lower.index(later)
                if later.islower():
                    result += self.calculate_letter(index, offset, Algorithm.alphabet_lower)
                else:
                    result += self.calculate_letter(index, offset, Algorithm.alphabet_upper)
            else:
                result = result + later
        return json.dumps({'result': result})

    @abstractmethod
    def calculate_letter(self, index: int, offset: int, alphabet: str) -> str:
        """
        Метод для дешифровки/шифровки буквы на основе её индекса в алфавите и смещения.
        """
        pass


class AlgorithmDecode(Algorithm):
    def calculate_letter(self, index: int, offset: int, alphabet: str) -> str:
        """
         '% len(alphabet)' используется для зацикливания обхода алфавита.
        """
        return alphabet[(index - offset) % len(alphabet)]


class AlgorithmEncode(Algorithm):
    def calculate_letter(self, index: int, offset: int, alphabet: str) -> str:
        """
        '% len(alphabet)' используется для зацикливания обхода алфавита.
        """
        return alphabet[(index + offset) % len(alphabet)]
