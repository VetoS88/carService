from django.urls import path

from cars.views import CarsAddView, CarRetrieveView

urlpatterns = [
    path('', CarsAddView.as_view(), name='addCar'),
    path('<int:serial_number>/', CarRetrieveView.as_view(), name='retrieveCar')
]
