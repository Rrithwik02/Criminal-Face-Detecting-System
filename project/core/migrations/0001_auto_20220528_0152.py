

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastface',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
