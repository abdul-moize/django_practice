# Generated by Django 3.2.7 on 2021-09-01 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.question')),
            ],
        ),
    ]
