from rest_framework import generics
from .serializer import EVCarSerializer
from .models import EV_Car
from .permissions import IsOwnerOrReadOnly


class EVCarList(generics.ListCreateAPIView):
    queryset = EV_Car.objects.all()
    serializer_class = EVCarSerializer

class EVCarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = EV_Car.objects.all()
    serializer_class = EVCarSerializer