# Generated by Django 4.1.2 on 2023-01-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_membership_active_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membershipdetail',
            options={'verbose_name_plural': 'price detail'},
        ),
        migrations.AddField(
            model_name='instructor',
            name='schedule',
            field=models.CharField(choices=[('senin', 'Senin'), ('selasa', 'Selasa'), ('rabu', 'Rabu'), ('kamis', 'Kamis'), ('jumat', 'Jumat')], default='senin', max_length=6),
        ),
    ]
