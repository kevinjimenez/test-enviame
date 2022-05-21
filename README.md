# NOMBRE PROYECTO: BACKEND DEVELOPER RETO

### Descripcion

El proyecto contiene dos microservices para un ecommerce y delivery

### Construccion
* **Language:** Python 3
* **Framework:** Flask, SQL Alchemy

## Requerimientos
- Docker

## Ejecucion

- Clonar repositorio.
- Crear un file **.env** 
- Copiar el contenido de file **.env.example** a **.env**, el cual contendra las variables de entorno para el ambiente local
- Tanto para ecommerce-service and delivery-services, dentro del directorio Docker/app
* Crear un file **.env** y copiar el contenido de file **.env.example** a **.env**

Para su ejecucion de forma local ejecutar el comando ```docker-compose up```

Los puerto por donde salen los microservices:
- ecommerce-service: 8000
- delivery-service: 8001