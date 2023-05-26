from django.urls import path 
from . import views 

app_name = 'todos'
urlpatterns = [
    # localhost:8000/todos/
    path('', views.index, name='index'),
    path('<int:pk>/complete/', views.complete, name='complete'),
]