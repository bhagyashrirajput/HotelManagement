# Generated by Django 3.2.3 on 2021-10-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_department_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]