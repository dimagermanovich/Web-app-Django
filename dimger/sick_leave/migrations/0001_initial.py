# Generated by Django 4.1.7 on 2023-04-17 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tableIncapables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('firstName', models.CharField(max_length=20, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_list', models.IntegerField(max_length=12, verbose_name='Номер листка нетрудоспособного')),
                ('name_of_organization', models.CharField(max_length=50, verbose_name='Название организации')),
                ('work', models.CharField(max_length=50, verbose_name='Должность')),
                ('ache', models.CharField(max_length=100, verbose_name='Болезнь')),
                ('begin_date', models.DateField(verbose_name='Начало больничного')),
                ('end_date', models.DateField(verbose_name='Конец больничного')),
                ('incapable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sick_leave.tableincapables')),
            ],
            options={
                'verbose_name': 'Лист',
                'verbose_name_plural': 'Листы',
            },
        ),
    ]
