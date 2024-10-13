from rest_framework import viewsets
from .serializer import BookModel, BookSerializer

# Create your views here.
class BookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer