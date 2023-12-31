# Generated by Django 4.2.5 on 2023-10-12 13:22

import albums.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(default='New Album', max_length=30)),
                ('creation_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation Date ')),
                ('release_datetime', models.DateTimeField(verbose_name='Release Date')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_approved', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.artist')),
            ],
            options={
                'order_with_respect_to': 'artist',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Song', max_length=50)),
                ('image', models.ImageField(upload_to='songs/images/%y/%m/%d')),
                ('audio', models.FileField(help_text='Allowed Extensions .mp3 , .wav', upload_to='songs/audio/%y/%m/%d', validators=[albums.models.validate_audio_file_extension])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
            ],
        ),
    ]
