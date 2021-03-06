from django.test import TestCase

from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),

            'Alan Turing',
            'http://hbn.link/turing-pic',
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),

        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_talk_link(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)


















