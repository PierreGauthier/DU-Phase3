# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.TimeField()),
                ('table', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
                ('old_value', models.CharField(max_length=100)),
                ('new_value', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Capteur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.TimeField()),
                ('type', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deviation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Infos_journalieres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('parking_access', models.IntegerField()),
                ('walker_access', models.IntegerField()),
                ('traffic_access', models.IntegerField()),
                ('noise_access', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isAnswer', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('civility', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roadwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('coord', models.CharField(max_length=50)),
                ('object', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=5000)),
                ('contact', models.ForeignKey(to='info_chantier.Pro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=200)),
                ('levelinfo', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='id_roadwork',
            field=models.ForeignKey(to='info_chantier.Roadwork'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='id_user',
            field=models.ForeignKey(to='info_chantier.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviation',
            name='id_roadwork',
            field=models.ForeignKey(to='info_chantier.Roadwork'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alert',
            name='id_roadwork',
            field=models.ForeignKey(to='info_chantier.Roadwork'),
            preserve_default=True,
        ),
    ]
