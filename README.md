# Despliegue de un Modelo de Machine Learning en Azure Container  
  
## Descripción del Proyecto  
  
Este proyecto consiste en el despliegue de un modelo de Machine Learning (ML) en Azure Container Instances. El objetivo es proveer un endpoint para hacer predicciones en tiempo real utilizando un modelo previamente entrenado.  
  
## Despliegue  
  
El despliegue consta de las siguientes etapas:  
  
1. **Construcción de la imagen Docker**: La imagen Docker se construye utilizando el Dockerfile proporcionado. Este proceso incluye la instalación de todas las dependencias listadas en `requirements.txt`.  
2. **Despliegue en Azure Container Instances**: Una vez construida la imagen Docker, se despliega en Azure Container Instances. Durante este proceso, se especifica el nombre DNS y se expone el puerto requerido.  
3. **Acceso al endpoint de predicción**: Una vez desplegado el contenedor, la aplicación puede ser accedida a través de la URL proporcionada por Azure Container Instances. Las predicciones pueden ser realizadas enviando una solicitud POST a la URL con los datos de entrada apropiados.  

## Tecnologías Utilizadas  
  
- Python  
- FastAPI  
- Docker  
- Azure Container Instances  
- Gunicorn/Uvicorn  
  
