# Generated by Django 2.1 on 2020-05-02 06:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('issue_start_date', models.DateField()),
                ('issue_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('Id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='issuer_id',
            field=models.ForeignKey(on_delete=models.SET(None), to='books.Issuer'),
        ),
    ]
