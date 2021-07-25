# Generated by Django 3.2.5 on 2021-07-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('C', 'Complete'), ('P', 'Pending'), ('F', 'Failed')], default='P', max_length=1),
        ),
    ]
