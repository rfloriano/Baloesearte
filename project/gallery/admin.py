from django.contrib import admin
from models import Photo, Gallery


class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    exclude = ["slug"]
    search_fields = ["label"]


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    exclude = ["slug"]

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)
