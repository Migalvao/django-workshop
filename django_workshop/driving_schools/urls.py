from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('schools/', views.schools_view, name='schools_list'),
    path('schools/<int:pk>/', views.single_school_view, name='single_school')
]
