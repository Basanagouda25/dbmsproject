# Generated by Django 5.2 on 2025-05-20 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_matches_teams_alter_allrounder_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allrounder',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allrounder', to='main.teams'),
        ),
        migrations.AlterField(
            model_name='batsmen',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batsmen', to='main.teams'),
        ),
        migrations.AlterField(
            model_name='bowlers',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bowlers', to='main.teams'),
        ),
    ]
