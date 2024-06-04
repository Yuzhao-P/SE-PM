

#<<<<<<< HEAD
# learn/urls.py【R12】
#=======
# learn/urls.py【R11】
#>>>>>>> C4
# learn/urls.py【R13】
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataCenter, name='DataCenter'),
]