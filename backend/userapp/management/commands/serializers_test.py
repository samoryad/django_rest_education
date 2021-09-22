import io

from django.core.management.base import BaseCommand
from rest_framework import serializers, renderers, parsers

# from library.models import Author


class Author:
    def __init__(self, first_name, last_name, birthday_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday_year = birthday_year

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday_year}'


class Bio:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __str__(self):
        return self.text


class Book:
    def __init__(self, title, authors):
        self.title = title
        self.authors = authors

    def __str__(self):
        return self.title


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        print('create')
        return Author(**validated_data)

    def update(self, instance, validated_data):
        print('update')
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.birthday_year = validated_data.get(
            'birthday_year', instance.birthday_year)
        return instance

    def validate_birthday_year(self, value):
        if value < 0:
            raise serializers.ValidationError('birthday_year must be positive')
        return value

    def validate(self, attrs):
        if attrs['last_name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
            raise serializers.ValidationError('1799')
        return attrs


class BioSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=64)
    author = AuthorSerializer()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    authors = AuthorSerializer(many=True)


class Command(BaseCommand):

    def handle(self, *args, **options):
        author = Author('Александр', 'Пушкин', 1799)
        author2 = Author('Александр', 'Грин', 1860)
        bio = Bio('Биография', author)
        book = Book('Книга', [author, author2])

        # serializer = AuthorSerializer(author)
        # serializer = BioSerializer(bio)
        serializer = BookSerializer(book)
        print(serializer.data)
        print(type(serializer.data))

        renderer = renderers.JSONRenderer()
        data_bytes = renderer.render(serializer.data)
        print(data_bytes)
        print(type(data_bytes))

        st = io.BytesIO(data_bytes)
        data = parsers.JSONParser().parse(st)
        print(data)
        print(type(data))

        # data = {
        #     'first_name': 'Александр',
        #     'last_name': 'Пушкин',
        #     'birthday_year': 100}
        data = {'birthday_year': 100}

        serializer = AuthorSerializer(author, data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            author = serializer.save()
            print(author)
        else:
            print(serializer.errors)
