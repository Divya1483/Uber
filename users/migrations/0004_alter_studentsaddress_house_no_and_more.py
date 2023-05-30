# Generated by Django 4.2 on 2023-05-30 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_studentsaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsaddress',
            name='house_no',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='street_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_addresses', to='users.students'),
        ),
    ]
