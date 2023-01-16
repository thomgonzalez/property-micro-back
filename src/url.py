from api.url import app_name, urlpatterns

BASE_API_URL = f"/{app_name}/"


def get_route():
    """
    Obtiene URL base para el Endpoint de Inmuebles
    """
    return BASE_API_URL + urlpatterns[0][0]
