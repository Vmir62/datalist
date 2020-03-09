from django.urls import path, include
from .import views
from .views import List
from.views import CustomersViewSet, SidelkiViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Customers',CustomersViewSet)
router.register('Sidelki',SidelkiViewSet)

urlpatterns = [
    path('', views.homepage),
    path('l1/', List.as_view()),
    path('customers/', include (router.urls)),
    path('sidelki/', include (router.urls)),
]

