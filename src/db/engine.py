# -*- coding: utf-8 -*-
from sqlalchemy import create_engine


class DataBase(object):
    """
    Clase para la conexión a la base de datos
    """

    def __init__(self, db_url):
        """
        Utilizaremos la función create_engine() para encender el motor MySQL
        """
        self.engine = create_engine(db_url)
        self._cnn = self.engine.connect()

    def execute(self, query):
        """
        Creamos el objeto conexión
        """
        rs = self._cnn.execute(query)
        return rs
