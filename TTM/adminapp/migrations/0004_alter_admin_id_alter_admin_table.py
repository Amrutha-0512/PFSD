# Generated by Django 5.0 on 2024-01-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_admin_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='admin',
            table='adminapp_admin',
        ),
    ]