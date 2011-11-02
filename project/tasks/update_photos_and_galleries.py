#! /usr/bin/env python

import os
import sys
import hashlib
import shutil
from datetime import datetime

aqui = os.path.abspath(os.path.split(__file__)[0])
acima = os.path.split(aqui)[0]
sys.path.append(acima)

from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.conf import settings
from gallery.models import Gallery, Photo

order = -1
albuns = []
for path, dirs, files in os.walk(settings.PHOTOS_PATH):
    if order == -1:
        albuns = dirs
    elif os.path.basename(path) == albuns[order]:
        gallery_name = albuns[order]
        gallery_hash = hashlib.sha256(gallery_name).hexdigest()

        gallery, gallery_created = Gallery.objects.get_or_create(gallery_hash=gallery_hash)

        for f in files:
            src = os.path.join(path, f)

            fh = open(src)
            h = hashlib.sha1()
            h.update(fh.read())
            image_hash = h.hexdigest()
            fh.close()

            try:
                photo = Photo.objects.get(image_hash=image_hash)
            except Photo.DoesNotExist:
                photo = Photo(image_hash=image_hash)

            if not photo.image:  # new photo
                dst_relative = os.path.join(photo.image.field.upload_to, f)
                dst = os.path.join(photo.image.storage.location, dst_relative)
                shutil.copy2(src, dst)
                fn, fe = os.path.splitext(os.path.basename(dst))
                photo.image = dst_relative
                photo.gallery = gallery
                photo.published_at = datetime.now()
                photo.name = fn
                photo.save()

        if gallery_created:  # new gallery
            gallery.name = gallery_name
            gallery.cover = photo
            gallery.save()

    order += 1
