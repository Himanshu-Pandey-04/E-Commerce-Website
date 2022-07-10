# Generated by Django 3.2.8 on 2022-02-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='no_picture.png', upload_to='')),
                ('MRP', models.PositiveIntegerField(default=0)),
                ('sellPrice', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]