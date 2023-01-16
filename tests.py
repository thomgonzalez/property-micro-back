# -*- coding: utf-8 -*-
import unittest
from src.settings import set_env
from src.db.config import get_database_url
from src.db.engine import DataBase

set_env()


def get_data(data):
    for row in data:
        yield row


class Test(unittest.TestCase):
    def setUp(self):
        self.engine = DataBase(get_database_url())

    def test_connexion(self):
        message = "El objeto dado no es una instancia de conexión."
        self.assertIsInstance(self.engine, object, message)

    def test_sql_selected(self):
        sql = """
        SELECT pr.id, pr.address, pr.city, pr.`year` ,  pr.price, pr.description, st.name, sh.id, sh.update_date 
        FROM status_history sh
        INNER JOIN property pr
            ON pr.id = sh.property_id 
        INNER  JOIN status st
            ON st.id = sh.status_id
        WHERE pr.id = (SELECT property_id FROM status_history WHERE property_id=pr.id ORDER BY id DESC LIMIT 1)
            AND pr.price <> 0  
            AND st.name IN ('pre_venta', 'en_venta', 'vendido')
            AND st.name= 'en_venta'
        """
        results = []
        data = self.engine.execute(sql)
        results = list(get_data(data))

        message = "La consulta como resultado debe contener datos."
        self.assertTrue(results, message)


if __name__ == "__main__":
    unittest.main()
