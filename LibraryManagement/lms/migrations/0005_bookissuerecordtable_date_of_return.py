# Generated by Django 4.1 on 2022-12-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_bookissuerecordtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookissuerecordtable',
            name='date_of_return',
            field=models.DateField(blank=True, null=True),
        ),
    ]
