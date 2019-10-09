from django.urls import path
from aplicaciones.encuestas import views
app_name='encuestas'
urlpatterns = [
    path('', views.index.as_view(), name='inicio'),
    path('listar_preguntas/', views.PreguntaList.as_view(), name='pregunta_list'),
    path('crear_preguntas/', views.PreguntaCreate.as_view(), name='pregunta_crear'),
    path('editar_preguntas/<int:pk>/', views.EditarPregunta.as_view(), name='pregunta_editar'),
    path('eliminar_preguntas/<int:pk>/', views.EliminarPregunta.as_view(), name='pregunta_eliminar'),
    path('eleccion/listar/', views.ListaEleccion.as_view(), name='eleccion_list'),
    path('delete_eleccion/<int:pk>/', views.DeleteEleccion.as_view(), name='eleccion_eliminar'),
    path('eleccion/crear/', views.EleccionCrear.as_view(), name='eleccion_crear'),
    path('eleccion/update/<int:pk>/', views.EleccionUpdate.as_view(), name='eleccion_update'),
]