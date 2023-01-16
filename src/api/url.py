# -*- coding: utf-8 -*-
from .view import InmuebleView

app_name = "api"

urlpatterns = [("inmuebles/", InmuebleView, "inmuebles_url")]
