# Pasos para instalación y ejecución del Proyecto

## 1. Clonamos el repositorio en nuestro local 
```bash
git clone https://github.com/reyalexander/sales-orders-challenge-2.git
```

## 2. Instalamos de nuestras dependencias y paquetes necesarios para el proyecto

```bash
pip freeze > requirements.txt
```

## 3. Creamos nuestra BD en PGAdmin y cambiamos los datos de la DATABASE y despues pasamos hacer las migracions

```py
python manage.py migrate
```

## 4. Creamos nuestro super usuario

```py
python manage.py createsuperuser

```
 
## 5. Y para poder correr el proyecto

```py
python manage.py runserver
```

[railway.app](https://railway.app/)

## 6. Para ver la documentacion con Swagger

- http://127.0.0.1:8000/swagger/
- http://127.0.0.1:8000/redoc/


## 5. Para probar los Endpoints

### Para hacer el CRUD de User
http://127.0.0.1:8000/user/

- Crear Usuario nuevo

```json
{
    "password": "rey12345",
    "username": "rey123",
    "first_name": "Cesar",
    "last_name": "Cuarite Silva",
    "email": "cesar@gmail.com",
    "is_staff": false,
    "is_active": true
}
```
### POST para obtener el token
http://127.0.0.1:8000/user/token/

- Modelo json de prueba
```json
{
 "username": "rey123",
 "password": "rey12345"
}
```

### Para hacer el CRUD de Order
http://127.0.0.1:8000/order/

- Modelo json de prueba
```json
{
    "order_code": "code555555",
    "total_price": "101.60",
    "status": "CANCELLED",
    "id_user": 1
}
```