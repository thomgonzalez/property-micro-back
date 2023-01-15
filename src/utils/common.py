import json


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
