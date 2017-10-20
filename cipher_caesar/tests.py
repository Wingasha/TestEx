from django.test import TestCase
from django.core.urlresolvers import reverse


"""
    Тесты на проверку правильного результата шифровки/дешифровки находятся уже в cipher_algorithm/tests.
    Так, что здесь нужно просто проверить работоспособность предствлений, отправляя запрос и ожидая ответ с кодом 200.
"""


class MainViewTests(TestCase):

    def test_main_page_view(self):
        response = self.client.get(reverse('cipher_caesar:main_page'))
        self.assertEqual(response.status_code, 200)

    def test_decode_view(self):
        response = self.client.post(reverse('cipher_caesar:decode'), data=b'{"text": "hello", "offset": "1"}',
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_encode_view(self):
        response = self.client.post(reverse('cipher_caesar:encode'), data=b'{"text": "hello", "offset": "1"}',
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
