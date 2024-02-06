import requests

def get_all_markets():
    """
    Fetches all markets from the Buda.com API.

    Returns:
        list: A list of all markets.
    """
    url = 'https://www.buda.com/api/v2/markets'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['markets']
    else:
        raise ValueError('An error occurred fetching markets')

def get_market_ticker(market_id):
    """
    Fetches the ticker information for a given market ID from the Buda.com API.

    Args:
        market_id (str): The market ID for which to fetch the ticker information.

    Returns:
        dict: The ticker information for the given market ID.
    """
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    
    if market_id not in [market['id'] for market in get_all_markets()]:
        raise ValueError('Invalid market ID')
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError('An error occurred fetching the ticker')

def calculate_spread(market_id):
    """
    Calculates the spread for a given market ID.

    Args:
        market_id (str): The market ID for which to calculate the spread.

    Returns:
        float: The spread for the given market ID.
    """
    ticker = get_market_ticker(market_id)
    if ticker and 'ticker' in ticker:
        max_bid = float(ticker['ticker']['max_bid'][0])
        min_ask = float(ticker['ticker']['min_ask'][0])
        spread = min_ask - max_bid
        return spread
    else:
        raise ValueError('Invalid ticker information')
    
def calculate_all_spreads():
    """
    Calculates the spread for all markets.

    Returns:
        list: A list of all spreads with name, id and spread.
    """
    markets = get_all_markets()
    spreads = []
    for market in markets:
        spread = calculate_spread(market['id'])
        if spread is not None:
            spreads.append({
                'id': market['id'],
                'spread': spread
            })
    return spreads
