# Generated by Django 3.2.8 on 2021-10-31 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0002_auto_20211031_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('img', models.ImageField(upload_to='creation', verbose_name='画像')),
                ('url', models.URLField(verbose_name='URL')),
                ('date', models.DateField(blank=True, null=True, verbose_name='公開日')),
            ],
            options={
                'verbose_name_plural': '作品集',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='本文')),
            ],
            options={
                'verbose_name_plural': 'スキルの詳細文',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='氏名')),
                ('img', models.ImageField(upload_to='proflie', verbose_name='画像')),
                ('career', models.CharField(blank=True, max_length=50, null=True, verbose_name='職業')),
                ('age', models.CharField(blank=True, max_length=50, null=True, verbose_name='年齢')),
                ('org', models.CharField(blank=True, max_length=50, null=True, verbose_name='所属組織')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='twitterURL')),
                ('introduce', models.TextField(verbose_name='自己紹介')),
            ],
            options={
                'verbose_name_plural': 'プロフィール',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='言語名')),
                ('period', models.FloatField(default=0, verbose_name='期間')),
                ('description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.description', verbose_name='説明文')),
            ],
        ),
    ]
