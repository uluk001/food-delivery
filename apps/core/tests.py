from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse



class ProductViewTestCase(TestCase):

    def test_view(self):
        path = reverse('base')  # 127.0.0.1:8000/base
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'Store')
        self.assertTemplateUsed(response, 'index.html')