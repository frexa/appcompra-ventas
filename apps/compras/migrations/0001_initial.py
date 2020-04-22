# Generated by Django 2.2.7 on 2020-04-22 01:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Código unico para cada compra', primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Código único para cada ingrediente', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('peso', models.FloatField(default=0.0)),
                ('precio_unit', models.FloatField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LineaDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('total', models.FloatField(default=0.0)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compra')),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Ingrediente')),
            ],
        ),
    ]
