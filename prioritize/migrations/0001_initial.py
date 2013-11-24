# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemSet'
        db.create_table(u'prioritize_itemset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('question', self.gf('django.db.models.fields.CharField')(default='Which is more important', max_length='100')),
        ))
        db.send_create_signal(u'prioritize', ['ItemSet'])

        # Adding model 'Item'
        db.create_table(u'prioritize_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=1000)),
            ('set', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['prioritize.ItemSet'])),
        ))
        db.send_create_signal(u'prioritize', ['Item'])


    def backwards(self, orm):
        # Deleting model 'ItemSet'
        db.delete_table(u'prioritize_itemset')

        # Deleting model 'Item'
        db.delete_table(u'prioritize_item')


    models = {
        u'prioritize.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['prioritize.ItemSet']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'prioritize.itemset': {
            'Meta': {'object_name': 'ItemSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'default': "'Which is more important'", 'max_length': "'100'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['prioritize']