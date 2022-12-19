#  MIKRO WAYS - Frameworks de desarrollo
El presente documento contiene los pasos necesarios para inicializar el backend el CRUD requerido en el ejercicio de Frameworks de desarrollo.

                
1. Descargar el respoitorio
2. Ingresar a la carpeta docker
3. Ejecutar docker-compose build
4. Ejecutar docker-compose up
                

El sistema no es más que un CRUD de una entidad denominada Car. Cada car posee tres atributos (name, brand y year).

Para crear un car:

curl -d '{"name":"Delta Integrale", "brand":"Lancia", "year": 1976}' -H "Content-Type: application/json" -X POST http://localhost:8005/api/car/

Para obtener el listado de cars:

curl  -X GET http://localhost:8005/api/car/

Para actualizar un car:

curl -d '{"name":"Palio", "brand":"Fiat", "year": 1996}' -H "Content-Type: application/json" -X PUT http://localhost:8005/api/car/1/ 

* el 1 que se observa en la url representa el id del recurso a actualizar. Colocar el que corresponda.

Para obtener un car:

curl -X GET http://localhost:8005/api/car/1/ 

* el 1 que se observa en la url representa el id del recurso a obtener. Colocar el que corresponda.

Para eliminar un car:

curl -X DELETE http://localhost:8005/api/car/1/

* el 1 que se observa en la url representa el id del recurso a obtener. Colocar el que corresponda.

El CRUD no requiere autenticación.

El endpoint /api/car/all_delete/ eliminar todos los cars del sistema. Este endpoint requiere autenticarse.  Para ello se debe realizar login con las siguientes credenciales

curl -d '{"user":"common__user", "password":"1234"}' -H "Content-Type: application/json" -X POST http://localhost:8005/login/ 

Este endpoint devolverá un token el cual debe utilizarse en la peticion a /api/car/all_delete/

curl -H "Authorization: Token 87031b3aa84546c0850a1025e672d34db3cd9999" -X DELETE http://localhost:8005/api/car/all_delete/

El endpoint /api/car/all_delete_with_permission/ eliminar todos los cars del sistema (lo mismo que el endpoint anterior). Este endpoint requiere un usuario con permisos los permisos adecuados,  para ello se debe realizar login con las siguientes credenciales

curl -d '{"user":"privileged__user", "password":"1234"}' -H "Content-Type: application/json" -X POST http://localhost:8005/login/ 

Este endpoint devolverá un token el cual debe utilizarse en la petición a /api/car/all_delete_with_permission/

curl -H "Authorization: Token 87031b3aa84546c0850a1025e672d34db3cd9999" -X DELETE http://localhost:8005/api/car/all_delete_with_permission/


Una pequeña documentacion de la api se puede observar desde:

http://127.0.0.1:8005/swagger/
