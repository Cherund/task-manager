# Generated by Django 5.0.7 on 2024-09-09 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0002_rename_timestamp_label_created_at'),
        ('statuses', '0002_rename_timestamp_status_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_tasks', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor_tasks', to=settings.AUTH_USER_MODEL, verbose_name='executor')),
                ('labels', models.ManyToManyField(blank=True, related_name='tasks', to='labels.label', verbose_name='labels')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='statuses.status', verbose_name='status')),
            ],
        ),
    ]