import json
from django.test import TestCase, Client
from .views import COMPONENTS

class OrderValidationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_create_valid_order(self):
        data = {"components": ["A", "D", "F", "I", "K"]}
        response = self.client.post('/api/orders', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("order_id", response.json())
        self.assertAlmostEqual(response.json()["total"], 142.3, places=2)
        expected_parts = ["LED Screen", "Wide-Angle Camera", "USB-C Port", "Android OS", "Metallic Body"]
        self.assertEqual(sorted(response.json()["parts"]), sorted(expected_parts))

    def test_create_invalid_order_missing_category(self):
        data = {"components": ["A", "D", "F", "I"]}
        response = self.client.post('/api/orders', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid order"})
        
    def test_create_invalid_order_duplicate_category(self):
        data = {"components": ["A", "D", "F", "I", "K", "B"]}
        response = self.client.post('/api/orders', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid order"})
        
    def test_create_invalid_order_unknown_component(self):
        data = {"components": ["A", "Z", "D", "F", "I", "K"]}
        response = self.client.post('/api/orders', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid order"})
        
    def test_create_valid_order_different_order(self):
        data = {"components": ["A", "I", "F", "D", "K"]}
        response = self.client.post('/api/orders', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("order_id", response.json())
        self.assertAlmostEqual(response.json()["total"], 142.3, places=2)  # Update to accurate total
        expected_parts = ["LED Screen", "Wide-Angle Camera", "USB-C Port", "Android OS", "Metallic Body"]
        self.assertEqual(sorted(response.json()["parts"]), sorted(expected_parts))  
        
    def test_create_invalid_order_missing_required_category(self):
        data = {"components": ["A", "D", "F", "K"]}
        response = self.client.post('/api/orders', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid order"})
