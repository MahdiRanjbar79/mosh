# Generated by Django 3.2.5 on 2021-07-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210724_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('F', 'Failed'), ('P', 'Pending'), ('C', 'Complete')], default='P', max_length=1),
        ),
    ]
