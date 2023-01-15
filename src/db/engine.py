# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI


class DataBase(object):
    """
    Clase para la conexión a la base de datos
    """

    def __init__(self):
        """
        Utilizaremos la función create_engine() para encender el motor MySQL
        """
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)

    def execute(self, query):
        """
        Creamos el objeto conexión
        """
        self._cnn = self.engine.connect()
        rs = self._cnn.execute(query)
        return rs
