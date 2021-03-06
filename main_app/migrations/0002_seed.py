# Generated by Django 4.0.4 on 2022-06-01 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_type', models.CharField(choices=[('bulb', 'Bulb'), ('seed', 'Seed'), ('tuber', 'Tuber'), ('corm', 'Corm'), ('rhyzome', 'Rhyzome')], default='seed', max_length=7)),
                ('seed_count', models.IntegerField(default=1)),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeds', to='main_app.flower')),
            ],
        ),
    ]
