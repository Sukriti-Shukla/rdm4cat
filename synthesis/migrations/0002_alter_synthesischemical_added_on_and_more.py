# Generated by Django 4.2.1 on 2023-06-09 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthesis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synthesischemical',
            name='added_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='synthesischemical',
            name='precursor_chemicals',
            field=models.JSONField(blank=True, null=True),
        ),
    ]