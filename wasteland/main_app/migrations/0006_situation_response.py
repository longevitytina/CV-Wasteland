# Generated by Django 3.0.5 on 2020-04-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200412_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='situation',
            name='response',
            field=models.CharField(choices=[('Run', 'Run'), ('Explore', 'Explore'), ('Fight', 'Fight'), ('Rest', 'Rest')], default='Run', max_length=20),
        ),
    ]
