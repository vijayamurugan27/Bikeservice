# Generated by Django 4.0.3 on 2022-04-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobslip', '0006_alter_customer_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='brand',
            field=models.CharField(choices=[('Royal enfield', 'Royal enfield'), ('KTM', 'KTM'), ('Yamaha', 'Yamaha'), ('TVS', 'TVS'), ('Bajaj', 'Bajaj'), ('Honda', 'Honda')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='warranty',
            field=models.CharField(choices=[('Yes', 'Yes'), ('Nil', 'Nil')], max_length=50),
        ),
    ]
