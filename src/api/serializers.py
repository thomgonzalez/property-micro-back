# -*- coding: utf-8 -*-
class InmuebleSerializer(object):
    """
    Clase base para serializar datos
    """

    _data = []

    def __init__(self, data):
        self.serializer(data)

    def serializer(self, data):
        """
        Recorrer datos y agrega en la lista
        """
        for row in data:
            self._data.append(
                {
                    "id": row.id,
                    "address": row.address,
                    "city": row.city,
                    "year": row.year,
                    "price": row.price,
                    "status": row.name,
                    "description": row.description,
                }
            )

    @property
    def data(self):
        """
        Propiedad de la clase para acceder a self._data
        """
        return self._data
