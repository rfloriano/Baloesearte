# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('gallery_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Gallery'])),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('image_hash', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('gallery', ['Photo'])

        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('cover', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cover_photo', null=True, to=orm['gallery.Photo'])),
            ('gallery_hash', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('gallery', ['Gallery'])


    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('gallery_photo')

        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')


    models = {
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cover_photo'", 'null': 'True', 'to': "orm['gallery.Photo']"}),
            'gallery_hash': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'gallery.photo': {
            'Meta': {'object_name': 'Photo'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['gallery']
