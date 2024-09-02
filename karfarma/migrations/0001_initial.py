# Generated by Django 5.1 on 2024-09-01 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karjoo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Karfarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('company_description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('salary', models.FloatField()),
                ('status', models.BooleanField()),
                ('karfarma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karfarma.karfarma')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('karjoo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karjoo.karjoo')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karfarma.offer')),
            ],
        ),
    ]
