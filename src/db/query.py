from db.engine import DataBase


def get_data():
    sql_raw = """SELECT pr.id, pr.description, st.name, st.label, sh.update_date 
        FROM status_history sh
        INNER JOIN property pr
            ON pr.id = sh.property_id 
        INNER  JOIN status st
            ON st.id = sh.status_id
        WHERE st.name IN ('pre_venta', 'en_venta', 'vendido')
    """

    db = DataBase()
    rs = db.execute(sql_raw)
    return rs
