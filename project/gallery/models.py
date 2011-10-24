from django.db import models
from django.core.urlresolvers import reverse


class Photo(models.Model):

    label = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='gallery/photos')
    published_at = models.DateTimeField(auto_now=True)
    image_hash = models.CharField(max_length=255)  # based on data image contet to know the image has been modified

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __unicode__(self):
        return self.label


class Gallery(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    cover = models.ForeignKey(Photo)
    gallery_hash = models.CharField(max_length=255)  # based on name to locate in database

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('viewname', urlconf=None, args=None, kwargs=None)
