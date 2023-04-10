# Challenge Back-End

A continuación se indicarán los pasos para correr correctamente el servidor y probar los endpoints desde Postman.

## Correr servidor

1. Lo primero que se debe realizar es instalar docker y docker-compose (en mi caso realicé la instalación de Docker Desktop en Windows que ya los incluye).
2. Se debe clonar este repositorio.
3. Se debe ejecutar el siguiente comando dentro del directorio raíz del proyecto para crear los contenedores y correrlos.

```bash
docker-compose up
```
4. Después de esto ya debería estar corriendo todo correctamente.

5. Para detener los contenedores se ejecuta el siguiente comando o con ctrl + C.

```bash
docker-compose down
```

## Probar los endpoints

1. Se debe importar la colección en Postman, la colección de postman se puede obtener del siguiente link :https://api.postman.com/collections/24722045-614772ff-ac92-4a56-b868-d7c0d5bf9db7?access_key=PMAT-01GXNHVB4NQE54ZT1620G181Z5  se debe dar en el botón import y pegar el link enviado, o se puede descargar directamente en el correo enviado con las respuestas de la prueba técnina, en este correo se encuentra el archivo de la colección (Se encuentra como respuesta del correo enviado)
2. Después, se debe crear un usuario (este endpoint se encuentra en la colección en la carpeta de Autenticación) para realizar la autenticación y poder consumir los servicios.
3. Ya con el usuario creado, se debe proceder a la autenticación, para lo cual se consumirá el endpoint del Login (se encuentra en la carpeta de Autenticación). Este retornará un response como el siguiente, del cual se tomará el access token:
```json
{
    "success": true,
    "detail": "Acción realizada con éxito",
    "data": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MTE2MTQ0MiwiaWF0IjoxNjgxMDc1MDQyLCJqdGkiOiIyZWU3ZWNjYzc4YTk0N2UxOTkzMWI1M2JhMjYxZWIwZSIsInVzZXJfaWQiOjF9.02gBmjyZ_P7T00gqhfjZoO3gs0NJFrydBozuZ50qX2E",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMTYxNDQyLCJpYXQiOjE2ODEwNzUwNDIsImp0aSI6ImYyZDM1ZTU2MWU4ZTQ1MThhNjg0MDc4M2FkNDdlNzA3IiwidXNlcl9pZCI6MX0.i6niY9lqMd8ofg8-rh3w5ZW2CW4boJQwyt1Rx4iQ3jA"
    }
}
```
4. Finalmente, se copia el access token retornado por el servicio anterior y se pega en la colección de Prueba en el parámetro de Token. Como ya todos los endpoints heredan esta autorización de la colección, deberían funcionar correctamente al realizar las peticiones.

## Consideraciones adicionales a la prueba

* Se agrego un EndPoint extra para filtar tareas por un rango de fechas.

* Se agregaron pruebas unitarias para algunos servicios, con el fin de demostrar mis conocimientos en la aplicación de estas.

* Se agrego la documentación técnica con swagger, se puede observar en el siguiente link:  http://127.0.0.1:8000/swagger/

* Se documento también cada EndPoint en Postman: https://documenter.getpostman.com/view/24722045/2s93XsYmHk


El asunto del correo enviado es: Prueba Técnica - Dev Python - Ciomprix Juan Camilo Arias
