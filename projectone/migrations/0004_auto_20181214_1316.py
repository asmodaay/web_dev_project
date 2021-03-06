# Generated by Django 2.1.4 on 2018-12-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectone', '0003_auto_20181214_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=120, verbose_name='Файл картинки')),
                ('artist_name', models.CharField(max_length=120, verbose_name='Имя исполнителя')),
                ('album_name', models.CharField(max_length=120, verbose_name='Название альбома')),
                ('release_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('description', models.TextField(verbose_name='Описание')),
                ('index', models.IntegerField(verbose_name='Индекс')),
            ],
        ),
        migrations.DeleteModel(
            name='Visual',
        ),
    ]
