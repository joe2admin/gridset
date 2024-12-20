# Generated by Django 5.1.4 on 2024-12-09 06:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('furniture', 'Furniture'), ('technology', 'Technology'), ('vehicles', 'Vehicles'), ('office_supplies', 'Office Supplies'), ('machinery', 'Machinery / Equipment')], max_length=50)),
                ('status', models.CharField(choices=[('available', 'Available'), ('in_use', 'In Use'), ('maintenance', 'Under Maintenance'), ('retired', 'Retired')], default='available', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='assets/')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_assets', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.department')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AssetRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.TextField(blank=True, help_text='Please explain why you need this asset', null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(blank=True, null=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='assets.asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-request_date'],
            },
        ),
    ]
