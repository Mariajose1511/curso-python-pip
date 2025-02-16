import unittest
import requests
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'countryName': 'United States of America',
            'regionName': 'California',
            'cityName': 'Mountain View',
            'countryCode': 'US',
            'continent': 'Americas',
        }

        result = get_location('8.8.8.8')

        self.assertEqual(result.get('country'), 'United States of America')
        self.assertEqual(result.get('region'), 'California')
        self.assertEqual(result.get('city'), 'Mountain View')
        self.assertEqual(result.get('code'), 'US')
        self.assertEqual(result.get('continent'), 'Americas')

        mock_get.assert_called_once_with('https://freeipapi.com/api/json/8.8.8.8')

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException('Service Unavailable'),
            requests.exceptions.HTTPError('Invalid IP address'),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    'countryName': 'United States of America',
                    'regionName': 'California',
                    'cityName': 'Mountain View',
                    'countryCode': 'US',
                    'continent': 'Americas',
                }
            )
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location('8.8.8.8')
        
        with self.assertRaises(requests.exceptions.HTTPError):
            get_location('9.9.9.9')

        result = get_location('8.8.8.8')
        self.assertEqual(result.get('country'), 'United States of America')
        self.assertEqual(result.get('region'), 'California')
        self.assertEqual(result.get('city'), 'Mountain View')
        self.assertEqual(result.get('code'), 'US')
        self.assertEqual(result.get('continent'), 'Americas')

    @patch('src.api_client.requests.get')
    def test_get_location_invalid_ip_raises_error(self, mock_get):        
        mock_get.side_effect = [
            requests.exceptions.HTTPError('Invalid IP address'),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    'countryName': 'United States of America',
                    'regionName': 'California',
                    'cityName': 'Mountain View',
                    'countryCode': 'US',
                    'continent': 'Americas',
                }
            )          
        ]

        with self.assertRaises(requests.exceptions.HTTPError):
            get_location('999.999.999.999')
        
        result = get_location('8.8.8.8')
        self.assertEqual(result.get('country'), 'United States of America')
        self.assertEqual(result.get('region'), 'California')
        self.assertEqual(result.get('city'), 'Mountain View')
        self.assertEqual(result.get('code'), 'US')
        self.assertEqual(result.get('continent'), 'Americas')

   