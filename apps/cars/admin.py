from django.contrib import admin

from cars.models import Car, MobileDeUrlPhoto


@admin.register(MobileDeUrlPhoto)
class MobileDeUlrPhotoAdmin(admin.ModelAdmin):
    pass


class CarInline(admin.TabularInline):
    model = Car
    fields = ('cars',)
    readonly_fields = ('cars',)

    def cars(self, obj):
        return '<a href="{}" >{}</a>'.format(obj.get_admin_url(), obj.title)

    cars.allow_tags = True


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'price', 'seller_info', 'images', 'seen')
    readonly_fields = (
        'title', 'url', 'price', 'seller_info', 'images', 'seen')

    def images(self, obj):
        html = ''
        for photo in obj.photos.all():
            html += '<img src="{}" width=200>'.format(photo.url)

        return html

    images.allow_tags = True
