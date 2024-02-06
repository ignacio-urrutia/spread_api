# tests/test_app.py

from flask_testing import TestCase
from app import create_app  # Ajusta esta línea para importar tu aplicación Flask correctamente
import requests_mock
# from unittest.mock import patch
from .mocks import MOCK_BTC_CLP_TICKER, MOCK_BTC_COP_TICKER, MOCK_ALL_MARKETS
from app.alert_spread import reset_alert_spreads

class SpreadTests(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    @requests_mock.Mocker()
    def test_get_market_spread(self, m):
        m.get('https://www.buda.com/api/v2/markets/BTC-CLP/ticker', json=MOCK_BTC_CLP_TICKER)
        m.get('https://www.buda.com/api/v2/markets', json=MOCK_ALL_MARKETS)
        response = self.client.get('/spreads/BTC-CLP')
        self.assert200(response)
        expected_spread = 50000.0
        self.assertEqual(response.json, {'spread': {'id': 'BTC-CLP', 'spread': expected_spread}})

    @requests_mock.Mocker()
    def test_get_all_market_spreads(self, m):
        m.get('https://www.buda.com/api/v2/markets/BTC-CLP/ticker', json=MOCK_BTC_CLP_TICKER)
        m.get('https://www.buda.com/api/v2/markets/BTC-COP/ticker', json=MOCK_BTC_COP_TICKER)
        m.get('https://www.buda.com/api/v2/markets', json=MOCK_ALL_MARKETS)
        response = self.client.get('/spreads')
        self.assert200(response)
        expected_spreads = [
            {'id': 'BTC-CLP', 'spread': 50000.0},
            {'id': 'BTC-COP', 'spread': 2000000.0}
        ]
        self.assertEqual(response.json, {'spreads': expected_spreads})

class AlertSpreadTests(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        super().setUp()
        reset_alert_spreads()

    def test_set_market_alert_spread(self):
        response = self.client.post('/alert_spreads/BTC-CLP/50000')
        self.assert200(response)
        self.assertEqual(response.json, {'alert_spreads': {'BTC-CLP': 50000.0}})

    @requests_mock.Mocker()
    def test_check_market_alert_spread(self, m):
        m.get('https://www.buda.com/api/v2/markets/BTC-CLP/ticker', json=MOCK_BTC_CLP_TICKER)
        m.get('https://www.buda.com/api/v2/markets', json=MOCK_ALL_MARKETS)
        
        self.client.post('/alert_spreads/BTC-CLP/50000')
        response = self.client.get('/alert_spreads/BTC-CLP')
        self.assert200(response)
        self.assertEqual(response.json, {'check_alerts': {'id': 'BTC-CLP','alarm': 50000.0, 'current_spread': 50000.0, 'current_spread_is_higher': False, 'current_spread_is_lower': False, 'current_spread_is_equal': True}})

    @requests_mock.Mocker()
    def test_check_market_alert_spread_value_error(self, m):
        m.get('https://www.buda.com/api/v2/markets', json=MOCK_ALL_MARKETS)
        response = self.client.get('/alert_spreads/INVALID-MARKET')
        self.assert400(response)
        self.assertEqual(response.json, {'error': 'Invalid market ID'})

    @requests_mock.Mocker()
    def test_get_all_market_alert_spreads(self, m):
        m.get('https://www.buda.com/api/v2/markets/BTC-CLP/ticker', json=MOCK_BTC_CLP_TICKER)
        m.get('https://www.buda.com/api/v2/markets/BTC-COP/ticker', json=MOCK_BTC_COP_TICKER)
        m.get('https://www.buda.com/api/v2/markets', json=MOCK_ALL_MARKETS)

        self.client.post('/alert_spreads/BTC-CLP/70000')
        self.client.post('/alert_spreads/BTC-COP/1000000')

        response = self.client.get('/alert_spreads')
        self.assert200(response)
        expected_response = {
            'alert_spreads': [
                {'id': 'BTC-CLP', 'alarm': 70000.0, 'current_spread': 50000.0, 'current_spread_is_higher': False, 'current_spread_is_lower': True, 'current_spread_is_equal': False},
                {'id': 'BTC-COP', 'alarm': 1000000.0, 'current_spread': 2000000.0, 'current_spread_is_higher': True, 'current_spread_is_lower': False, 'current_spread_is_equal': False}
            ] 
        }
        self.assertEqual(response.json, expected_response)

