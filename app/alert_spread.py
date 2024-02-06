from .buda_api import calculate_spread, get_all_markets

alert_spreads = {}

def set_alert_spread(market_id, value):
    if market_id not in [market['id'] for market in get_all_markets()]:
        raise ValueError('Invalid market ID')
    alert_spreads[market_id] = float(value)
    return alert_spreads

def get_alert_spread(market_id):
    if market_id not in [market['id'] for market in get_all_markets()]:
        raise ValueError('Invalid market ID')
    if market_id not in alert_spreads:
        raise ValueError('Alert spread not set')
    return alert_spreads.get(market_id)
    
def get_all_alert_spreads():
    return alert_spreads

def check_alert_spread(market_id):
    spread = calculate_spread(market_id)
    if market_id not in alert_spreads:
        raise ValueError('Alert spread not set')
    alert_spread = get_alert_spread(market_id)
    current_spread_is_higher = spread > alert_spread
    current_spread_is_lower = spread < alert_spread
    current_spread_is_equal = spread == alert_spread
    return {'id': market_id, 'alarm': alert_spread, 'current_spread': spread, 'current_spread_is_higher': current_spread_is_higher, 'current_spread_is_lower': current_spread_is_lower, 'current_spread_is_equal': current_spread_is_equal}

def reset_alert_spreads():
    alert_spreads.clear()
    return alert_spreads
