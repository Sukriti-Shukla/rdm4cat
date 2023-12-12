# Generated by Django 4.2.1 on 2023-06-06 15:29

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labitemtype', models.CharField(max_length=100)),
                ('labitemsubtype', models.CharField(max_length=100)),
                ('labitemid', models.IntegerField()),
                ('labitemname', models.CharField(max_length=100)),
                ('documents', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('files', models.FileField(blank=True, null=True, upload_to='docs/')),
                ('json_data', models.JSONField(blank=True, null=True)),
                ('additional_fields', models.TextField(blank=True, null=True)),
                ('custom_fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]