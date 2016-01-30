from django.contrib import admin

from cars.models import Car, MobileDeUrlPhoto


@admin.register(MobileDeUrlPhoto)
class MobileDeUlrPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'price', 'seller_info', 'images')
    readonly_fields = ('title', 'url', 'price', 'seller_info', 'images')

    def images(self, obj):
        html = ''
        for photo in obj.photos.all():
            html += '<img src="{}" width=200 style="ma">'.format(photo.url)

        return html

    images.allow_tags = True
