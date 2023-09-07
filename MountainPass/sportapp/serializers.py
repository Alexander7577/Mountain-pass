from rest_framework import serializers
from .models import PerevalAdded, User, Coords, Image, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PerevalAddedSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    images = ImageSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        coords_data = validated_data.pop('coords')

        author, created = User.objects.get_or_create(**author_data)
        coords = Coords.objects.create(**coords_data)
        category = Category.objects.create(**category_data)
        images = Image.objects.create(**images_data)

        pereval_added = PerevalAdded.objects.create\
            (author=author, coords=coords, images=images, category=category, **validated_data)
        return pereval_added
