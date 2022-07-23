# Generated by Django 3.1 on 2020-09-13 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0002_auto_20200905_0748'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_ordered',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='complete',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='date_added',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
