# Generated by Django 4.2.5 on 2023-09-23 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company')),
            ],
        ),
    ]