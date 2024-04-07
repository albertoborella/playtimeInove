# Generated by Django 4.0 on 2024-02-14 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_articulo_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='stock.articulo'),
        ),
    ]
