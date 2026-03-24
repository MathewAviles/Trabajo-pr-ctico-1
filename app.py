from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL de la API pública de ESPN para La Liga (esp.1)
ESPN_API_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard"

@app.route('/api/laliga/live', methods=['GET'])
def get_live_scores():
    try:
        response = requests.get(ESPN_API_URL)
        response.raise_for_status()
        data = response.json()
        
        matches = []
        for event in data.get('events', []):
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            # Identificar local y visitante
            home_team = next((team for team in competitors if team.get('homeAway') == 'home'), None)
            away_team = next((team for team in competitors if team.get('homeAway') == 'away'), None)
            
            # Respaldos por si la API cambia su estructura levemente
            if not home_team and len(competitors) > 0: home_team = competitors[0]
            if not away_team and len(competitors) > 1: away_team = competitors[1]
            
            match_info = {
                'id': event.get('id'),
                'name': event.get('name'),
                'shortName': event.get('shortName'),
                'date': event.get('date'),
                'status': event.get('status', {}).get('type', {}).get('description', 'Desconocido'),
                'time': event.get('status', {}).get('displayClock', ''),
                'period': event.get('status', {}).get('period', 0),
                'home_team': home_team.get('team', {}).get('displayName', 'Local') if home_team else 'Local',
                'home_score': home_team.get('score', '0') if home_team else '0',
                'away_team': away_team.get('team', {}).get('displayName', 'Visitante') if away_team else 'Visitante',
                'away_score': away_team.get('score', '0') if away_team else '0',
            }
            matches.append(match_info)
            
        return jsonify({
            'success': True,
            'league': data.get('leagues', [{}])[0].get('name', 'La Liga'),
            'season': data.get('season', {}).get('year'),
            'matches': matches
        })
        
    except requests.RequestException as e:
        return jsonify({
            'success': False,
            'error': f"Error al obtener los datos: {str(e)}"
        }), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensaje": "API de Resultados de La Liga",
        "endpoints": {
            "resultados en vivo": "/api/laliga/live"
        }
    })

if __name__ == '__main__':
    # Inicia el servidor de desarrollo de Flask
    app.run(debug=True, port=5000)
