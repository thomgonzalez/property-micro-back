# -*- coding: utf-8 -*-
from src.api.view import InmuebleView

app_name = "api"

urlpatterns = [("inmuebles/", InmuebleView, "inmuebles_url")]
