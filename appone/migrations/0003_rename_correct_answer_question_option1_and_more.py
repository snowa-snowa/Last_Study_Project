# Generated by Django 5.1.4 on 2025-02-28 08:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_test_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='correct_answer',
            new_name='option1',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
