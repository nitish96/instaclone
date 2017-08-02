from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170718_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='phone',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='age',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='gender',
        ),
    ]