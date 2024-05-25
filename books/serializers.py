from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price']

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # agar title va author raqamlardan tashkil topkan bolsa qabul qilmayda
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitobni sarlavhasi xarflardan tashkil topkan bolishi kerak"
                }
            )

        # title va author birxil bolsa qabul qilmaydi
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Author va Sarlavxasi birxil bolgan kitopni kiritolmaysiz"
                }
            )
        # Return the validated data
        return data

    def validate_price(self, price):
        if price < 0 or price > 999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Narx notogri kiritilgan"
                }
            )
