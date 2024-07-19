from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


from ovqat.models import Food, Category
from ovqat.permissions import IsOwnerOrReadOnly
from ovqat.serializers import FoodSerializers, CategorySerializers


class Createfood(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class Listfood(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]

class Updatefood(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]


class Deletefood(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

class Createcategory(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]

class Listcategory(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers


class Updatecategory(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]


class Deletecategory(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]