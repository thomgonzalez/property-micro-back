from db.engine import DataBase


def parse_params(data):
    """
    Método parse query params.
    """
    year = data.get("year")[0] if data.get("year") else None
    city = data.get("city")[0] if data.get("city") else None
    status = data.get("status")[0] if data.get("status") else None
    return {"year": year, "city": city, "status": status}


def filters(kwargs):
    """ "
    Método para consulta con filtros opcionales.
    """
    params = parse_params(kwargs)
    year = params.get("year")
    city = params.get("city")
    status = params.get("status")
    sql_raw = ""

    if year:
        sql_raw = f" AND pr.year = {year}"

    if city:
        sql_raw = f" AND pr.city = '{city}'"

    if status:
        sql_raw = f" AND st.name = '{status}'"

    if year and city:
        sql_raw = f" AND pr.year = {year} AND pr.city = '{city}'"

    if year and status:
        sql_raw = f" AND pr.year = {year} AND st.name = '{status}'"

    if city and status:
        sql_raw = f" AND pr.city = '{city}' AND st.name = '{status}'"

    if year and city and status:
        sql_raw = (
            f" AND pr.year = {year} AND pr.city = '{city}' AND st.name = '{status}'"
        )

    return sql_raw


def get_data(**kwargs):
    """
    Método forma SQL para ejecutar por SQLAlchemy
    nativo con conexion a la base de datos MySQL.
    """
    query_filter = ""
    query_filter = filters(kwargs)
    sql_raw = """SELECT pr.id, pr.address, pr.city, pr.`year`, pr.price, pr.description, 
        st.name, sh.id, sh.update_date 
        FROM status_history sh
        INNER JOIN property pr
            ON pr.id = sh.property_id 
        INNER  JOIN status st
            ON st.id = sh.status_id
        WHERE pr.id = (SELECT property_id FROM status_history 
            WHERE property_id=pr.id ORDER BY id DESC LIMIT 1)
                AND pr.price <> 0  
                AND st.name IN ('pre_venta', 'en_venta', 'vendido')
    """
    sql_raw += query_filter
    db = DataBase()
    rs = db.execute(sql_raw)
    return rs
