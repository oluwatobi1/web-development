# Generated by Django 3.0.3 on 2020-07-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='password',
            field=models.CharField(default='nothing', max_length=45),
        ),
    ]