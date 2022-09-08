from django.urls import path
from .views import EVCarList, EVCarDetail

urlpatterns = [
    path('', EVCarList.as_view(), name='evcars_list'),
    path('/<int:pk>', EVCarDetail.as_view(), name='evcar_detail')
]