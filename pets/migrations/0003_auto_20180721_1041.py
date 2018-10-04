# Generated by Django 2.0.6 on 2018-07-21 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_searchresults_search_inst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresults',
            name='search_inst',
        ),
        migrations.AddField(
            model_name='searchresults',
            name='search',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.Search'),
        ),
        migrations.AlterField(
            model_name='search',
            name='interest',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='pet_breed_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.Pet_Breed'),
        ),
        migrations.AlterField(
            model_name='search',
            name='pet_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.Pet_Type'),
        ),
    ]
