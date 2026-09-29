from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from api.models import Genre, Book

class GenreAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genre_list = []

        for genre in genres:
            genre_list.append(
                {
                    "id" : genre.id,
                    "name": genre.name,
                    "description": genre.description
                }
            )
        return Response(genre_list)

    def post(self, request):
        genre = Genre.objects.create(**request.data)
        genre_dict = model_to_dict(genre)
        return Response(genre_dict, status=201)

class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        book_list = []

        for book in books:
            book_list.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "description": book.description,
                    "price": book.price,
                    "genres": [
                        {
                            "id": genre.id,
                            "name": genre.name
                        }
                        for genre in book.genres.all()
                    ]
                }
            )

        return Response(book_list)

    def post(self, request):
        book = Book.objects.create(**request.data)
        book_dict = model_to_dict(book)
        return Response(book_dict, status=201)

    