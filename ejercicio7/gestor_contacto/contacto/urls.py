
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_lista, name='contacto_lista'),
    path('agregar/', views.contacto_agregar, name='contacto_agregar'),
    path('actualizar/<int:pk>', views.contacto_actualizar, name='contacto_actualizar'),
    path('eliminar/<int:pk>/', views.contacto_eliminar, name='contacto_eliminar'),
]
