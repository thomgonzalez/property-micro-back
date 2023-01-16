# -*- coding: utf-8 -*-
from db.query import get_data
from api.serializers import InmuebleSerializer
from utils.common import to_encode, to_json


class InmuebleView(object):
    """
    Clase API para inmuebles
    """

    def get(self, **kwargs):
        """
        Método obtiene lista de propiedades
        """
        # Obtener datos en objectos
        result = get_data(**kwargs)
        # Serialización de datos
        serializer = InmuebleSerializer(data=result)
        data = serializer.data
        response = to_encode(to_json({"status": 200, "data": data}))
        return response
