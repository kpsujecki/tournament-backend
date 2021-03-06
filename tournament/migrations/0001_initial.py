# Generated by Django 3.2.4 on 2021-06-29 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration', models.DurationField()),
                ('winning_score', models.PositiveIntegerField()),
                ('losing_score', models.PositiveIntegerField()),
                ('round', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('start_time', models.DateField(blank=True, null=True)),
                ('amountUsers', models.IntegerField(default=0)),
                ('isFinished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.match')),
            ],
        ),
    ]
