from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Author(models.Model):
    gender_choice = (
        ("M","Male"),
        ("F", "Female")
    )
    name = models.CharField(max_length=32,verbose_name="作者姓名")
    age = models.IntegerField(verbose_name="作者年龄",blank=True,null=True)
    gender = models.CharField(max_length=2,choices=gender_choice,verbose_name="作者性别",blank=True,null=True)
    email = models.EmailField(verbose_name="作者邮箱")
    phone = models.CharField(max_length=11,verbose_name="作者电话",blank=True,null=True)
    photo = models.ImageField(verbose_name="作者头像",upload_to="images/author")

    def __str__(self):
        return "作者：%s"%self.name

class Classify(models.Model):
    label = models.CharField(max_length=32,verbose_name="分类标签")
    description = RichTextUploadingField(verbose_name="分类描述")

    def __str__(self):
        return "标签：%s"%self.label

class Comment(models.Model):
    content = RichTextUploadingField(verbose_name="评论内容")
    content_name = models.CharField(max_length=32, verbose_name="用户姓名")
    agree = models.IntegerField(verbose_name="评论点赞")
    time = models.DateTimeField(verbose_name="评论时间")

    def __str__(self):
        return "[%s] 评论 %s"%(self.content_name,self.content)

class Picture(models.Model):
    label = models.CharField(max_length=32,verbose_name="图片名称")
    image = models.ImageField(verbose_name="图片链接",upload_to="images/picture")
    description = RichTextUploadingField(verbose_name="图片描述")

    classify = models.ForeignKey(to=Classify,verbose_name="图片分类")
    comment = models.ForeignKey(to=Comment, verbose_name="图片评论")

    def __str__(self):
        return "图片名称：%s"%self.label

class ArticleManager(models.Manager):
    """
    返回文章的总数
    定义一个查询集
    """
    def article_count(self,keyword=""):
        return self.filter(title__icontains = keyword).count() #__icontains进行数据模糊查询 类似like,双下划线

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="文章标题")
    time = models.DateField(verbose_name="文章发表日期")

    description = RichTextUploadingField(verbose_name="文章的描述")
    content = RichTextUploadingField(verbose_name="文章内容")

    picture = models.ImageField(verbose_name="文章图片",upload_to="images/picture")

    author = models.ForeignKey(Author)
    classify = models.ManyToManyField(to=Classify,verbose_name="文章分类")
    comment = models.ForeignKey(to=Comment,verbose_name="文章评论",blank=True,null=True)

    objects = ArticleManager()
    def __str__(self):
        return "文章：%s"%self.title

    def valid_title(self):
        """
        定义查询集
        :return:
        """
        title = self.title  # 获取title字段的内容
        if "习近平" in title:  # 进行判断返回指定结果
            return "这个文章牛"
        else:
            return "一般般吧"
