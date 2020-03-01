from django.urls import path
from .import views
from .views import List


urlpatterns = [
    path('', views.homepage),
    path('l1/', List.as_view()),
]