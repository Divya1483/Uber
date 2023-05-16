from django.urls import path,include
from .views import *
from users.views import *


urlpatterns = [
    path('get-all-students',GetStudentsView.as_view()),
    path('get-and-save-order',GetOrdersView.as_view()),
]

