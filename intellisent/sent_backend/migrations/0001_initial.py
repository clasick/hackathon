# Generated by Django 2.0 on 2018-03-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('tweet_id', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('text', models.CharField(max_length=300)),
                ('replies', models.IntegerField()),
                ('retweets', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('hashtags', models.CharField(max_length=200)),
                ('tweet_class', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]