# API Resultados de La Liga (Tiempo Real)

Esta es una API simple en Python con Flask que obtiene los resultados y el estado en tiempo real de los partidos de la liga española de fútbol (La Liga). Utiliza una ruta pública de ESPN que no requiere "API Key", lo cual la hace gratuita y fácil de usar inmediatamente.

## Requisitos Previos

Asegúrate de tener Python instalado en tu máquina. Luego instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

*(Es recomendable usar un entorno virtual `venv` aunque no es obligatorio).*

## Arrancar la API

Para levantar el servidor localmente, simplemente ejecuta:

```bash
python app.py
```

El servidor iniciará en: `http://127.0.0.1:5000/`

## Endpoints Disponibles

### 1. Índice
- **URL**: `/`
- **Method**: `GET`
- **Descripción**: Muestra un mensaje de bienvenida y los endpoints disponibles.

### 2. Resultados en Vivo (La Liga)
- **URL**: `/api/laliga/live`
- **Method**: `GET`
- **Descripción**: Retorna la lista de partidos del día o de la jornada en curso para La Liga española. Obtendrás información del estado del partido (terminado, en vivo, por jugar), los nombres de los equipos y su marcador en tiempo real.

#### Ejemplo de Respuesta:
```json
{
  "league": "Spanish LALIGA",
  "matches": [
    {
      "away_score": "2",
      "away_team": "Real Madrid",
      "date": "2024-03-02T20:00Z",
      "home_score": "2",
      "home_team": "Valencia",
      "id": "692882",
      "name": "Valencia vs. Real Madrid",
      "period": 2,
      "shortName": "VAL vs RMA",
      "status": "Canceled",
      "time": "90'"
    }
  ],
  "season": 2023,
  "success": true
}
```

## Tecnologías Utilizadas
- **Python 3**
- **Flask**: Framework web para construir la API rápidamente.
- **Requests**: Librería para realizar las peticiones HTTP a la información pública deportiva.
