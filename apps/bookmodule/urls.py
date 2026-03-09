from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<int:val>/',views.index2),
    path('<int:bookID>', views.viewbook)
]
