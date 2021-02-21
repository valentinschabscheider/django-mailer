# Generated by Django 3.0.10 on 2021-02-21 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0003_auto_20210221_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='sent',
        ),
        migrations.CreateModel(
            name='Outbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.Mail')),
            ],
        ),
    ]
