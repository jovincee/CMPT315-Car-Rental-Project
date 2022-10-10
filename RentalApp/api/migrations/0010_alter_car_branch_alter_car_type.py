# Generated by Django 4.1.1 on 2022-10-09 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_branch_branchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.branch'),
        ),
        migrations.AlterField(
            model_name='car',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cartype'),
        ),
    ]
