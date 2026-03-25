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

## Endpoints Disponibles

### 1. Índice
- **URL**: `/`
- **Method**: `GET`
- **Descripción**: Muestra un mensaje de bienvenida y los endpoints disponibles.

---

### 2. Resultados en Vivo (La Liga)
- **URL**: `/api/laliga/live`
- **Method**: `GET`
- **Descripción**: Retorna la lista de partidos del día o de la jornada en curso para La Liga española. Incluye estado del partido, equipos, marcador, tiempo y período.
- **Parámetros opcionales**:
  - `team` (query): Filtra los partidos por nombre de equipo.

**Ejemplo:**
```bash
GET /api/laliga/live?team=Barcelona
```

---

### 3. Agregar Equipo Favorito
- **URL**: `/api/laliga/favorite`
- **Method**: `POST`
- **Descripción**: Permite agregar un equipo a la lista de favoritos.

**Body (JSON):**
```json
{
  "team": "Barcelona"
}
```

**Respuestas:**
- `201 Created`: Equipo agregado correctamente.
- `400 Bad Request`: Error en los datos enviados.

---

### 4. Obtener Equipos Favoritos
- **URL**: `/api/laliga/favorite`
- **Method**: `GET`
- **Descripción**: Retorna la lista de equipos favoritos almacenados en memoria.

**Ejemplo de respuesta:**
```json
{
  "success": true,
  "favorites": ["Barcelona", "Real Madrid"]
}
```

## Tecnologías Utilizadas
- **Python 3**
- **Flask**: Framework web para construir la API rápidamente.
- **Requests**: Librería para realizar las peticiones HTTP a la información pública deportiva.

# EVIDENCIA
## API funcionando localmente


## Construcción de imagen Docker


## Contenedor ejecutándose


## Prueba curl exitosa


## API desplegada en Cloud


## Endpoint accesible públicamente

