from drf_yasg import openapi
from login.serializers import LoginSerializer


post_login = {
    'responses': {
        '201': openapi.Response(
            'Operacion exitosa. response: { token : "token"}'),
        '400': "Petición inválida\n"
    },
    'operation_id': "Realizar login en el sistema para obtener el token de\
        autenticacion.",
    'operation_description': "Realizar login en el sistema para obtener el \
        token de autenticacion. El token debe ser enviado en el header de cada\
        request: \
            'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b '\
        ",
    'request_body': LoginSerializer()
}

get_logout = {
    'responses': {
        '200': openapi.Response('Operacion exitosa.'),
    },
    'operation_id': "Elimina el token del usuario.",
    'operation_description': "Elimina el token del usuario.",
}
