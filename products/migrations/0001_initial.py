# Generated by Django 5.2.4 on 2025-07-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cameralar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('resolution', models.CharField(default='24MP', max_length=20)),
                ('zoom', models.CharField(default='20x', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('image', models.ImageField(blank=True, default='default/camere.jpg', null=True, upload_to='camera-image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updates_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
