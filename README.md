# Development and Deployment of a Machine Learning Model in Azure Container with CI/CD using GitHub Actions
  
## Project Description  
This project involves the deployment of a Machine Learning model in Azure Container Instances. The objective is to provide an endpoint for making real-time predictions using a previously trained model and automate machine learning operations.
   
## Deployment  
The deployment consists of the following stages: 
  
1. **Docker Image Construction**: The Docker image is built using the provided Dockerfile. This process includes the installation of all dependencies listed in `requirements.txt`.  
2. **Deployment in Azure Container Instances**: Once the Docker image is built, it is deployed in Azure Container Instances. During this process, the DNS name is specified and the required port is exposed.  
3. **Access to the prediction endpoint**: Once the container is deployed, the application can be accessed through the URL provided by Azure Container Instances. Predictions can be made by sending a POST request to the URL with the appropriate input data.  

## Technologies Used  
- Python  
- FastAPI  
- Docker  
- Azure Container Instances  
- Gunicorn/Uvicorn  
  
