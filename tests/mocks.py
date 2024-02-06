MOCK_BTC_CLP_TICKER = {
    "ticker": {
        "last_price": ["879789.0", "CLP"],
        "market_id": "BTC-CLP",
        "max_bid": ["800000.0", "CLP"],
        "min_ask": ["850000.0", "CLP"],
        "price_variation_24h": "0.005",
        "price_variation_7d": "0.1",
        "volume": ["102.0", "BTC"]
    }
}

MOCK_BTC_COP_TICKER = {
    "ticker": {
        "last_price": ["165397503.99", "COP"],
        "market_id": "BTC-COP",
        "max_bid": ["163000000.0", "COP"],
        "min_ask": ["165000000.0", "COP"],
        "price_variation_24h": "0.005",
        "price_variation_7d": "0.1",
        "volume": ["102.0", "BTC"]
    }
}

MOCK_ALL_MARKETS = {
    "markets": [{
        "id": "BTC-CLP",
        "name": "btc-clp",
        "base_currency": "BTC",
        "quote_currency": "CLP",
        "minimum_order_amount": ["0.001", "BTC"],
        "taker_fee": "0.8",
        "maker_fee": "0.4",
        "max_orders_per_minute":100,
        "maker_discount_percentage":"0.0",
        "taker_discount_percentage":"0.0"
    },
    {
        "id": "BTC-COP",
        "name": "btc-cop",
        "base_currency": "BTC",
        "quote_currency": "COP",
        "minimum_order_amount": ["0.001", "BTC"],
        "taker_fee": "0.8",
        "maker_fee": "0.4",
        "max_orders_per_minute":100,
        "maker_discount_percentage":"0.0",
        "taker_discount_percentage":"0.0"
    }]
}
