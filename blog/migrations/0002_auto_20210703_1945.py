# Generated by Django 3.2.4 on 2021-07-03 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.topic')),
            ],
        ),
        migrations.RemoveField(
            model_name='accessdate',
            name='content',
        ),
        migrations.DeleteModel(
            name='content',
        ),
        migrations.AddField(
            model_name='accessdate',
            name='text',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.text'),
            preserve_default=False,
        ),
    ]
