# Generated by Django 4.1 on 2022-12-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_bookissuerecordtable_date_of_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
