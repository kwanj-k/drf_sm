# Generated by Django 2.1.7 on 2019-07-02 10:23

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('packaging', models.CharField(max_length=20)),
                ('package_pices', models.IntegerField()),
                ('number_of_packages', models.IntegerField()),
                ('package_price', models.IntegerField()),
                ('piece_price', models.IntegerField()),
                ('number_of_pieces', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
    ]
