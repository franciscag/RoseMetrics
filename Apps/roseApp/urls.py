
# '======[Importaciones]============================'
from django.contrib import admin
from django.urls import path

from Apps.roseApp.views import *
from Apps.roseApp.views import *
# '==============================================='

# °===========================°
#    °URLs -> roseApp
# °===========================°

from django.urls import path
from Apps.roseApp.views import *


urlpatterns = [

    path('registrar-meses/', registrarMeses, name='registrar_meses'),

    path('resultados/', resultados, name='resultados'),

]




