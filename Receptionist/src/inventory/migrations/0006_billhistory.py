# Generated by Django 2.0.7 on 2020-11-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20201112_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mob_no', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
