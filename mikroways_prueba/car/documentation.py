from drf_yasg import openapi
from car.serializers import CarSerializer

retrieve = {
    'responses': {
        '200': openapi.Response('Operacion exitosa.', CarSerializer())
    },
    'operation_id': "Obtener un Car en específico del sistema.",
    'operation_description': "Obtener un Car en específico del sistema.",
}

list_car = {
    'responses': {
        '200': openapi.Response('Operacion exitosa.', CarSerializer(many=True))
    },
    'operation_id': "Obtener todos los Cars del sistema.",
    'operation_description': "Obtener todos los Cars del sistema.",
}


create = {
    'responses': {
        '201': openapi.Response(
            'Operacion exitosa.',
            CarSerializer()
        ),
        '400': "Petición inválida\n"
    },
    'operation_id': "Crear un Car en el sistema.",
    'operation_description': "Crear un Car en el sistema",
    'request_body': CarSerializer()
}

update = {
    'responses': {
        '200': openapi.Response('Operacion exitosa.', CarSerializer())
    },
    'operation_id': "Actualizar un Car del sistema.",
    'operation_description': "Actualizar un Car del sistema.",
    'request_body': CarSerializer()
}


delete = {
    'responses': {
        '204': openapi.Response('Operacion exitosa.'),
    },
    'operation_id': "Elimina un Car específico del sistema.",
    'operation_description': "Elimina un Car específico del sistema.",
}

delete_all = {
    'responses': {
        '204': openapi.Response('Operacion exitosa.'),
    },
    'operation_id': "Elimina todos los cars del sistema.",
    'operation_description': "Elimina todos los cars del sistema.",
}

delete_all_with_permission = {
    'responses': {
        '204': openapi.Response('Operacion exitosa.'),
    },
    'operation_id': "Elimina todos los cars del sistema.",
    'operation_description': "Elimina todos los cars del sistema.",
}
