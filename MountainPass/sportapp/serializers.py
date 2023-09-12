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
    data = serializers.CharField()

    class Meta:
        model = Image
        fields = ('data', 'title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PerevalUpdateSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ImageSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        exclude = ('author',)

    def update(self, instance, validated_data):
        if instance.status != 'new':
            raise serializers.ValidationError("Редактирование разрешено только для записей со статусом 'new'.")

        # Обновление полей модели PerevalAdded
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.area = validated_data.get('area', instance.area)
        instance.type_activity = validated_data.get('type_activity', instance.type_activity)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.status = validated_data.get('status', instance.status)

        # Обновление связанных объектов (вложенных сериализаторов)
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        coords_data = validated_data.pop('coords')

        coords, created = Coords.objects.get_or_create(**coords_data)
        category, created = Category.objects.get_or_create(**category_data)
        images, created = Image.objects.get_or_create(**images_data)

        # Обновление связей с вложенными объектами
        instance.coords = coords
        instance.category = category
        instance.images = images

        instance.save()

        return instance


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

