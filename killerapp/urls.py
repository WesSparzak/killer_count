from django.urls import path
from .views import main, update_counter

urlpatterns = [
    path('main/', main, name='main'),
    path('update_counter/<int:killer_id>/', update_counter, name='update_counter'),
    path('', main, name='main'),
]
