from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.adminP),
    path('add',views.addPage),
    path('addProduct',views.addP),
    path('deleteP/<int:id>',views.deleteP),
    path('viewOrder',views.OrderH)
]
