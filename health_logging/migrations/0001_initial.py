# Generated by Django 5.1.3 on 2024-11-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.FloatField()),
                ('glucose', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('skin_thickness', models.FloatField()),
                ('insulin', models.FloatField()),
                ('bmi', models.FloatField()),
                ('diabetes_pedigree_function', models.FloatField()),
                ('age', models.FloatField()),
                ('diabetes_prediction', models.FloatField()),
                ('date_created', models.DateField()),
            ],
        ),
    ]