from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):

  class Meta:
    model = Book
    fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)

  def validate(self, data):
    title = data.get('title', None)
    author = data.get('author', None)

    # check title
    if not title.isalpha():
      raise ValidationError(
        {
          "status": False,
          "message": "Please, check your data!"
        }
      )

    # check author&title
    if Book.objects.filter(title=title, author=author).exists():
      raise ValidationError(
        {
          "status": False,
          "message": "Kitob sarlavhasi va mualliffi bir xil."
        }
      )
    return data

  def validate_price(self, price):
    if price < 0 or price > 999999999:
      raise ValidationError(
        {
          "status": False,
          "message": "Narx noto'g'ri kiritilgan."
        }
      )

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#     author = serializers.CharField(max_length=100)
#     isbn = serializers.CharField(max_length=13)
#     price = serializers.DecimalField(max_digits=20, decimal_places=2)

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.subtitle = validated_data.get('subtitle', instance.subtitle)
#         instance.content = validated_data.get('content', instance.content)
#         instance.author = validated_data.get('author', instance.author)
#         instance.isbn = validated_data.get('isbn', instance.isbn)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance

#     def validate_price(self, value):
#         if value <= 0:
#             raise serializers.ValidationError("Narx musbat bo‘lishi kerak.")
#         return value

#     def validate_isbn(self, value):
#         if not value.isdigit():
#             raise serializers.ValidationError("ISBN faqat raqamlardan iborat bo‘lishi kerak.")
#         if len(value) != 13:
#             raise serializers.ValidationError("ISBN uzunligi 13 ta belgidan iborat bo‘lishi kerak.")
#         return value
