# -*- coding: utf-8 -*-
from url import get_route
from api.view import InmuebleView
from utils.common import to_json, to_encode, get_query_params


url = get_route()


def default_reponse():
    """
    Respuesta Default
    """
    response = {"status_code": 200, "message": "Property Micro - API Rest"}
    # Conversion de datos en formato json y codificación en UTF-8
    return [to_encode(to_json(response))]


def notfound_response():
    """
    Respuesta de rutas no encontradas
    """
    response = {"status_code": 404, "message": "Not Found"}
    # Conversion de datos en formato json y codificación en UTF-8
    return [to_encode(to_json(response))]


def application(environ, start_response):
    """
    Una aplicación WSGI básica
    """
    http_status = "200 OK"
    headers = [("Content-type", "application/json")]
    PATH_INFO = environ["PATH_INFO"]
    QUERY_STRING = environ["QUERY_STRING"]

    start_response(http_status, headers)

    if PATH_INFO == "/":
        return default_reponse()

    if PATH_INFO == url:
        params = get_query_params(QUERY_STRING)
        view = InmuebleView()
        response = view.get(**params)
        # Response del Api
        return [response]

    else:
        return notfound_response()
