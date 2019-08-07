# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='文章标题', max_length=32)),
                ('time', models.DateField(verbose_name='文章发表日期')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章的描述')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('picture', models.ImageField(verbose_name='文章图片', upload_to='images/picture')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='作者姓名', max_length=32)),
                ('age', models.IntegerField(null=True, verbose_name='作者姓名', blank=True)),
                ('gender', models.CharField(max_length=2, blank=True, null=True, verbose_name='作者性别', choices=[('M', 'Male'), ('F', 'Female')])),
                ('email', models.EmailField(verbose_name='作者邮箱', max_length=254)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='作者电话', blank=True)),
                ('photo', models.ImageField(verbose_name='作者头像', upload_to='images/author')),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('label', models.CharField(verbose_name='分类标签', max_length=32)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='分类描述')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='评论内容')),
                ('content_name', models.CharField(verbose_name='用户姓名', max_length=32)),
                ('agree', models.IntegerField(verbose_name='评论点赞')),
                ('time', models.DateTimeField(verbose_name='评论时间')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('label', models.CharField(verbose_name='图片名称', max_length=32)),
                ('image', models.ImageField(verbose_name='图片链接', upload_to='images/picture')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='图片描述')),
                ('classify', models.ForeignKey(to='app01.Classify', verbose_name='图片分类',on_delete=models.CASCADE)),
                ('comment', models.ForeignKey(to='app01.Comment', verbose_name='图片评论',on_delete=models.CASCADE)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='app01.Author',on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='article',
            name='classify',
            field=models.ManyToManyField(to='app01.Classify', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(to='app01.Comment', blank=True, verbose_name='文章评论', null=True,on_delete=models.CASCADE),
        ),
    ]
