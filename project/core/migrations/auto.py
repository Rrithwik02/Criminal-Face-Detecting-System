

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age',
            new_name='date',
        ),
    ]
