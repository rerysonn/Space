from django import path 
from galeria.views import index

urlpatterns = [
    path('', index)    
]
