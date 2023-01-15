import json
from url import get_route
from api.view import InmuebleView

url = get_route()


def application(environ, start_response):
    """
    Una aplicación WSGI básica
    """
    http_status = "200 OK"
    headers = [("Content-type", "application/json")]

    start_response(http_status, headers)

    if environ["PATH_INFO"] == url:
        view = InmuebleView()
        data = view.get()
        print("APi....", data)

    # respuesta
    response = {"message": "Property Micro - API Rest"}
    # Conversion en Bytes data response y codificación en UTF-8
    return [bytes(json.dumps(response), "UTF-8")]
