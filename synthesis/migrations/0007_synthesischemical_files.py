# Generated by Django 4.2.1 on 2023-06-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthesis', '0006_synthesischemical_additional_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='synthesischemical',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
    ]
