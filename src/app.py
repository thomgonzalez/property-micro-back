import json
from wsgiref.simple_server import make_server


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


if __name__ == "__main__":
    print("Serving on port 8000...")
    # Respond to requests
    make_server("localhost", 8000, application).serve_forever()
