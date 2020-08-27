# Generated by Django 3.1 on 2020-08-27 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('filed_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('ticket_status', models.CharField(choices=[('N', 'new'), ('IP', 'in_progress'), ('D', 'done'), ('INV', 'invalid')], default='N', max_length=3)),
                ('user_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_assigned', to=settings.AUTH_USER_MODEL)),
                ('user_completed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_completed', to=settings.AUTH_USER_MODEL)),
                ('user_filed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_filed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
