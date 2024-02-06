from flask import Blueprint, jsonify
# from flasgger import swag_from
from .buda_api import calculate_spread, calculate_all_spreads
from .alert_spread import set_alert_spread, get_alert_spread, get_all_alert_spreads, check_alert_spread

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Un simple endpoint de bienvenida
    ---
    tags:
      - Bienvenida
    responses:
      200:
        description: Mensaje de bienvenida
        examples:
          application/json: {"message": "Welcome to Ignacio Urrutia's Spread API proxy!"}
    """
    return jsonify({"message": "Welcome to Ignacio Urrutia's Spread API proxy!"})

@main.route('/spreads/<market_id>')
def get_market_spread(market_id):
    """
    Obtener el spread para un mercado específico
    ---
    tags:
      - Spreads
    parameters:
      - in: path
        name: market_id
        type: string
        required: true
        description: El ID del mercado (por ejemplo, 'BTC-CLP')
    responses:
      200:
        description: El spread del mercado solicitado
        schema:
          type: object
          properties:
            spread:
              type: object
              properties:
                id:
                  type: string
                  example: BTC-CLP
                spread:
                  type: number
                  example: 100.1
      400:
        description: Error en la solicitud, como un ID de mercado no válido
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'Invalid market ID'
    """
    try:
        spread = calculate_spread(market_id)
        return jsonify({'spread': {'id': market_id, 'spread': spread}}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@main.route('/spreads')
def get_all_market_spreads():
    """
    Obtener los spreads de todos los mercados
    ---
    tags:
      - Spreads
    responses:
      200:
        description: Una lista de los spreads de todos los mercados
        schema:
          type: object
          properties:
            spreads:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                    example: btc-clp
                  spread:
                    type: number
                    example: 100.0
      400:
        description: Error al obtener los spreads de los mercados
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'An error occurred fetching the spreads'
              """
    try:
        spreads = calculate_all_spreads()
        return jsonify({'spreads': spreads}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@main.route('/alert_spreads/<market_id>/<value>', methods=['POST'])
def set_market_alert_spread(market_id, value):
    """
    Establece un spread de alerta para un mercado específico
    ---
    tags:
      - Alert Spreads
    parameters:
      - in: path
        name: market_id
        type: string
        required: true
        description: El ID del mercado para el cual se establece la alerta
      - in: path
        name: value
        type: number
        required: true
        description: El valor del spread para establecer la alerta
    responses:
      200:
        description: Dicctioario con todos los spreads de alerta establecidos, llave market_id, valor value
        schema:
          type: object
          properties:
            alert_spreads:
              type: object
              properties:
                BTC-CLP:
                  type: number
                  example: 100.0
      400:
        description: Error en la solicitud, como un ID de mercado no válido o un valor incorrecto
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'Invalid market ID'
    """

    try:
        alert_spreads = set_alert_spread(market_id, value)
        return jsonify({'alert_spreads': alert_spreads}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@main.route('/alert_spreads/<market_id>', methods=['GET'])
def check_market_alert_spread(market_id):
    """
    Consulta el spread de alerta para un mercado específico
    ---
    tags:
      - Alert Spreads
    parameters:
      - in: path
        name: market_id
        type: string
        required: true
        description: El ID del mercado para el cual se consulta la alerta
    responses:
      200:
        description: Información de la alerta de spread para el mercado solicitado
        schema:
          type: object
          properties:
            check_alerts:
              type: object
              properties:
                id:
                  type: string
                  example: btc-clp
                alarm:
                  type: number
                  example: 100.0
                current_spread:
                  type: number
                  example: 105.0
                current_spread_is_higher:
                  type: boolean
                  example: true
                current_spread_is_lower:
                  type: boolean
                  example: false
                current_spread_is_equal:
                  type: boolean
                  example: false
      400:
        description: Error en la solicitud, como un ID de mercado no válido
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'Invalid market ID'
    """

    try:
        check_alerts = check_alert_spread(market_id)
        return jsonify({'check_alerts': check_alerts}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@main.route('/alert_spreads', methods=['GET'])
def get_all_market_alert_spreads():
    """
    Obtiene los spreads de alerta para todos los mercados
    ---
    tags:
      - Alert Spreads
    responses:
      200:
        description: Lista de todos los spreads de alerta establecidos
        schema:
          type: object
          properties:
            alert_spreads:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                    example: btc-clp
                  alarm:
                    type: number
                    example: 100.0
                  current_spread:
                    type: number
                    example: 105.0
                  current_spread_is_higher:
                    type: boolean
                    example: true
                  current_spread_is_lower:
                    type: boolean
                    example: false
                  current_spread_is_equal:
                    type: boolean
                    example: false
      400:
        description: Error al obtener los spreads de alerta
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'An error occurred fetching alert spreads'
    """

    try:
        alert_spreads = get_all_alert_spreads()
        alert_spreads_list = []
        for market_id, value in alert_spreads.items():
            alert_spreads_list.append(check_alert_spread(market_id))
        return jsonify({'alert_spreads': alert_spreads_list}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

