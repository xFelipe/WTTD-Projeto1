from django.test import TestCase
from django.shortcuts import render, resolve_url as r


class SpeakerDetailTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/palestrantes/grace-hopper/')

    def test_get(self):
        """GET Should return status 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)