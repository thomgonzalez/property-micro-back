# -*- coding: utf-8 -*-
import json
from urllib.parse import parse_qs


def to_json(data):
    """
    Metodo que convierte datos en formato Json.
    """
    rs = json.dumps(data)
    return rs


def to_encode(data):
    """
    Metodo que codifica en UTF-8
    """
    return data.encode("UTF-8")


def get_query_params(parse_result):
    """
    Obtener parámetros de consulta por URL
    """
    dict_qp = parse_qs(parse_result)
    return dict_qp
