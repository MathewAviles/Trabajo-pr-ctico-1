# API Reporte de Daños Técnicos

Proyecto desarrollado con FastAPI.

## Funcionalidades
- Crear reportes
- Consultar reportes
- Actualizar reportes

## Tecnologías
- Python
- FastAPI
- Docker
- GitHub
  
## Ejecución con Docker

```bash
docker build -t api-reportes-danos .
docker run -p 8080:8080 api-reportes-danos
```

## Despliegue en la nube
El despliegue en Google Cloud Run no se completó debido a la necesidad de habilitar facturación en la plataforma.
Sin embargo, el proyecto se encuentra completamente preparado para despliegue, ya que cuenta con un Dockerfile funcional y una imagen de contenedor que ejecuta correctamente el API.
El sistema puede ser desplegado en cualquier entorno cloud compatible con contenedores.
