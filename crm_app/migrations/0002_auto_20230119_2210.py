# Generated by Django 3.2.5 on 2023-01-19 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='posistion',
            new_name='position',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_counter',
        ),
    ]