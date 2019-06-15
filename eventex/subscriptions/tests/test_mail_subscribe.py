from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Felipe Gomes', cpf='12345678901',
                    email='felipegd@gmail.com', phone='21-99618-6180')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid post should redirect to /inscricao/"""
        self.assertEqual(302, self.response.status_code)  # redirect

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'felipegd@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Felipe Gomes',
            '12345678901',
            'felipegd@gmail',
            '21-99618-6180',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        # self.assertIn('Felipe Gomes', self.email.body)
        # self.assertIn('12345678901', self.email.body)
        # self.assertIn('felipegd@gmail.com', self.email.body)
        # self.assertIn('21-99618-6180', self.email.body)