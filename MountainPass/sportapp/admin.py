from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Coords, Image, Category, PerevalAdded


class PerevalAddedAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'author', 'area', 'beauty_title', 'title', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.images.data:
            return mark_safe(f'<img src={obj.images.data.url} width="50" height="60">')
        else:
            return

    get_image.short_description = 'Изображение'


admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(PerevalAdded, PerevalAddedAdmin)
