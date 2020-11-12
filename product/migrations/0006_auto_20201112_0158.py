# Generated by Django 3.1.3 on 2020-11-11 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_accessoris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATpearent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATpearent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='main category'),
        ),
        migrations.AlterField(
            model_name='product_accessoris',
            name='PACCAlternative',
            field=models.ManyToManyField(related_name='alternativeACCESSORS_products', to='product.Product', verbose_name='Accessoris'),
        ),
        migrations.AlterField(
            model_name='product_accessoris',
            name='PACCproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainACCESSORS_product', to='product.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNAlternative',
            field=models.ManyToManyField(related_name='alternative_products', to='product.Product', verbose_name='Alternatve'),
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product', verbose_name='product'),
        ),
    ]
