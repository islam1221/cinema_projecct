from collections import defaultdict
from rest_framework import serializers
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import CinemaSerializer, MovieSerializer,MovieDetailSerializers
from .models import Cinema, Movie
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

@api_view(['GET', 'POST'])
def index(request):
    data = {
        'integer':100,
        'float':10.0,
        'boolean': False,
        'list': [1,2,3],
        'text': 'hello world'
    }
    return Response(data=data)


class CinemaListAPIView(ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class CinemaDetailAPIView(RetrieveAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    lookup_field = 'id'

@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        products = Movie.objects.all()
        serializer = MovieSerializer(products, many =True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data['title']
        description = request.data('description')
        cinema = request.data.get('cinema')
        genres = request.data.get('genres', [])
        movie = Movie.objects.create(
            title=title,description=description,cinema=cinema,genres_id=genres,
        )
        movie.genres.set(genres)
        movie.save()
        return Response()

@api_view(['GET','PUT','DELETE'])
def moviedetailview(request,id):
    try:
        product = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
        data={'error': 'Product not Found!'})
    if request.method == 'GET':
        serializer = MovieDetailSerializers(product, many =False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        product.title = request.data['title']
        product.description = request.data['description']
        product.cinema_id = request.data['cinema']
        product.genres.set(request.data['genres'])
        product.save()
        return Response(data={'message':'Product updated!'})
    else:
        product.delete()
        return Response

# Create your views here.
