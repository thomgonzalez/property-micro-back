import json


def application(environ, start_response):
    """
    Una aplicación WSGI básica
    """
    http_status = "200 OK"
    headers = [("Content-type", "application/json")]

    start_response(http_status, headers)

    # respuesta
    response = {"message": "Property Micro - API Rest"}
    # Conversion en Bytes data response y codificación en UTF-8
    return [bytes(json.dumps(response), "UTF-8")]
