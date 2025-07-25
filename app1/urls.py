from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.add,name='add'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]