from .algorithm import AlgorithmDecode, AlgorithmEncode
import unittest


class AlgorithmJSONTest(unittest.TestCase):

    def test_decode_encode_methods(self):
        """
        Тестирует правильность шифровки и дешифровки текста
        """
        result_decode = AlgorithmDecode().get_json_result(json_factory('hello', '1'))
        result_encode = AlgorithmEncode().get_json_result(json_factory('hello', '1'))
        self.assertEqual(result_decode, '{"result": "gdkkn"}')
        self.assertEqual(result_encode, '{"result": "ifmmp"}')

    def test_decode_encode_with_empty_text(self):
        """
        Если во входном объекте отсутствует текс для шифровки/дешифровки, то в результирующем объекте будет
        отсутствовать текст
        """
        result_decode = AlgorithmDecode().get_json_result(json_factory('', '1'))
        result_encode = AlgorithmEncode().get_json_result(json_factory('', '1'))
        self.assertEqual(result_decode, '{"result": ""}')
        self.assertEqual(result_encode, '{"result": ""}')

    def test_decode_encode_with_empty_offset(self):
        """
        Если во входном объекте отсутствует значение смещения для шифровки/дешифровки, то в результирующем объекте будет
        отсутствовать текст
        """
        result_decode = AlgorithmDecode().get_json_result(json_factory('hello', ''))
        result_encode = AlgorithmEncode().get_json_result(json_factory('hello', ''))
        self.assertEqual(result_decode, '{"result": ""}')
        self.assertEqual(result_encode, '{"result": ""}')

    def test_decode_encode_with_empty_offset_and_text(self):
        """
        Если во входном объекте отсутствует текст и значение смещения для шифровки/дешифровки, то в результирующем
        объекте будет отсутствовать текст
        """
        result_decode = AlgorithmDecode().get_json_result(json_factory('', ''))
        result_encode = AlgorithmEncode().get_json_result(json_factory('', ''))
        self.assertEqual(result_decode, '{"result": ""}')
        self.assertEqual(result_encode, '{"result": ""}')

    def test_decode_encode_with_offset_below_zero(self):
        """
        Если во входном объекте отсутствует значение смещения для шифровки/дешифровки меньше нуля, то в результирующем
        объекте будет отсутствовать текст
        """
        result_decode = AlgorithmDecode().get_json_result(json_factory('', '-1'))
        result_encode = AlgorithmEncode().get_json_result(json_factory('', '-1'))
        self.assertEqual(result_decode, '{"result": ""}')
        self.assertEqual(result_encode, '{"result": ""}')

    def test_decode_encode_with_large_offset(self):
        """
        Если значение смещения больше количества букв в алфавите, то дальше начинаются повторения
        """
        result_decode = AlgorithmDecode().get_json_result(json_factory('hello', '27'))
        result_encode = AlgorithmEncode().get_json_result(json_factory('hello', '27'))
        self.assertEqual(result_decode, '{"result": "gdkkn"}')
        self.assertEqual(result_encode, '{"result": "ifmmp"}')


def json_factory(text: str, offset: str) -> bytes:
    """
    Фабричный метод, который принимает в качестве аргументов строку и смещение.
    Возвращает JSON-объект в виде байт-строки.
    """
    return ('{"text": "%s", "offset": "%s"}' % (text, offset)).encode()


if __name__ == '__main__':
    unittest.main()
