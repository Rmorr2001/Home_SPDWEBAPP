# Generated by Django 4.2.18 on 2025-01-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_membership_status_membership_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brother',
            name='membership_status',
        ),
        migrations.RemoveField(
            model_name='dashboard_link',
            name='membership_status',
        ),
        migrations.DeleteModel(
            name='Membership_Status',
        ),
        migrations.AddField(
            model_name='brother',
            name='membership_status',
            field=models.CharField(choices=[('New Member', 'New Member'), ('Active', 'Active'), ('Active Exec', 'Active Exec'), ('Alumni', 'Alumni'), ('Alumni Exec', 'Alumni Exec')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dashboard_link',
            name='membership_status',
            field=models.CharField(choices=[('New Member', 'New Member'), ('Active', 'Active'), ('Active Exec', 'Active Exec'), ('Alumni', 'Alumni'), ('Alumni Exec', 'Alumni Exec')], max_length=200, null=True),
        ),
    ]
