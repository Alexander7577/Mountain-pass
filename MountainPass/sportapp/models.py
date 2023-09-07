from django.db import models
from .data.choices import LEVELS, BEAUTYTITLE, PEREVALAREAS, TYPEACTIVITY, STATUSES


class User(models.Model):
    email = models.EmailField(max_length=50)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return f'{self.latitude}° {self.longitude}° {self.height}М'


class Image(models.Model):
    data = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    winter = models.CharField(max_length=2, choices=LEVELS)
    spring = models.CharField(max_length=2, choices=LEVELS)
    summer = models.CharField(max_length=2, choices=LEVELS)
    autumn = models.CharField(max_length=2, choices=LEVELS)

    def __str__(self):
        return f'зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}'


class PerevalAdded(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(choices=BEAUTYTITLE, max_length=120)
    title = models.CharField(max_length=150)
    other_titles = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    area = models.CharField(choices=PEREVALAREAS, max_length=50)
    type_activity = models.CharField(choices=TYPEACTIVITY)
    connect = models.CharField(max_length=250)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=30, default='new')
