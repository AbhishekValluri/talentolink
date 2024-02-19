# Generated by Django 4.2.10 on 2024-02-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0002_alter_contact_table_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=100)),
                ('Companyname', models.CharField(max_length=150)),
                ('Numofvacancies', models.BigIntegerField()),
                ('location', models.CharField(max_length=100, null=True)),
                ('Jobdescription', models.CharField(max_length=150, null=True)),
                ('Salary', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]