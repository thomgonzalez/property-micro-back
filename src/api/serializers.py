
class InmuebleSerializer(object):
    """
    Clase base para serializar datos
    """
    _data = []
    def __init__(self, data):
        self.serializer(data)

    def serializer(self, data):
        for row in data:
            self._data.append({
                'id': row.id,
                'description': row.description
            })

    @property
    def data(self):
        return self._data
