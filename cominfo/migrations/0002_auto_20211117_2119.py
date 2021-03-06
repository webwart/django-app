# Generated by Django 3.2.7 on 2021-11-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cominfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyinfo',
            options={'ordering': ['-stars_count', 'company']},
        ),
        migrations.RenameField(
            model_name='companyinfo',
            old_name='title',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='category_id',
            field=models.IntegerField(choices=[(1, 'Asia'), (2, 'S-Afrika'), (3, 'N-Afrika'), (4, 'C-Amerika')]),
        ),
    ]
