# Generated by Django 2.2.1 on 2019-06-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receiverName', models.CharField(max_length=30)),
                ('senderName', models.CharField(max_length=30)),
                ('receiverAddress', models.CharField(max_length=50)),
                ('senderAddress', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('kind', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
