from django.test import TestCase
from .models import Quote

class QuoteTests(TestCase):
    def test_pages(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/all/').status_code, 200)
        self.assertEqual(self.client.get('/api/quote/').status_code, 200)
    def test_crud(self):
        response = self.client.post('/api/quotes/', {'text': 'Test', 'author': 'Student'}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        url = f"/api/quotes/{response.json()['id']}/"
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.put(url, {'text': 'Changed'}, content_type='application/json').json()['text'], 'Changed')
        self.assertEqual(self.client.delete(url).status_code, 200)
        self.assertEqual(self.client.get(url).status_code, 404)
