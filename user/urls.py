from django.urls import path
from .views import CreateUserView, VerifyApi

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('verify/', CreateUserView.as_view(), name='VerifyApi'),

]