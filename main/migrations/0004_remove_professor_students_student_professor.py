# Generated by Django 4.2.2 on 2023-06-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_professor_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='professor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.professor'),
            preserve_default=False,
        ),
    ]