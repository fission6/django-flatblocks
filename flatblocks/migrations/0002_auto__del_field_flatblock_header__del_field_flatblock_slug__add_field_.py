# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FlatBlock.header'
        db.delete_column('flatblocks_flatblock', 'header')

        # Deleting field 'FlatBlock.slug'
        db.delete_column('flatblocks_flatblock', 'slug')

        # Adding field 'FlatBlock.namespace'
        db.add_column('flatblocks_flatblock', 'namespace', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255), keep_default=False)

        # Adding field 'FlatBlock.description'
        db.add_column('flatblocks_flatblock', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'FlatBlock.header'
        db.add_column('flatblocks_flatblock', 'header', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'FlatBlock.slug'
        raise RuntimeError("Cannot reverse this migration. 'FlatBlock.slug' and its values cannot be restored.")

        # Deleting field 'FlatBlock.namespace'
        db.delete_column('flatblocks_flatblock', 'namespace')

        # Deleting field 'FlatBlock.description'
        db.delete_column('flatblocks_flatblock', 'description')


    models = {
        'flatblocks.flatblock': {
            'Meta': {'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'namespace': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['flatblocks']
