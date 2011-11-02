from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Photo(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/gallery/photos')
    gallery = models.ForeignKey('Gallery')
    published_at = models.DateTimeField(auto_now=True)
    image_hash = models.CharField(max_length=255)  # based on data image contet to know the image has been modified

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __unicode__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('viewname', urlconf=None, args=None, kwargs=None)


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    cover = models.ForeignKey(Photo, null=True, blank=True, related_name='cover_photo')
    gallery_hash = models.CharField(max_length=255)  # based on name to locate in database

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('viewname', urlconf=None, args=None, kwargs=None)


def slugify_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(slugify_pre_save, sender=Photo)
signals.pre_save.connect(slugify_pre_save, sender=Gallery)
