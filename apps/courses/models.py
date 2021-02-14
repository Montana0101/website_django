from apps.users.models import BasicModel
from apps.organizations.models import Teacher
from django.db import models

degree = (
    ('cj','初级'),
    ('zj','中级'),
    ('gj','高级')
)
class Course(BasicModel):
    teacher = models.ForeignKey(Teacher,verbose_name='讲师',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='课程名称',max_length=50)
    desc = models.CharField(verbose_name='课程描述',max_length=300)
    learn_times = models.IntegerField(verbose_name='学习时长',default=0)
    degree = models.CharField(verbose_name='难度',choices=degree,max_length=10)
    students = models.IntegerField(verbose_name='学习人数',default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数',default=0)
    click_nums = models.IntegerField(verbose_name='点击数',default=0)
    category = models.CharField(default='前端开发',max_length=20,verbose_name='课程类别')
    tag = models.CharField(default='', verbose_name='课程标签',max_length=10)
    need_know = models.CharField(default='',max_length=200,verbose_name='课程须知')
    teacher_tell = models.CharField(default='',max_length=300,verbose_name='老师告诉你')
    
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(verbose_name='封面图',upload_to='course/%Y/%m', height_field=None, width_field=None, max_length=200)
    
    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

class Lesson(BasicModel):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(verbose_name='章节名称',max_length=300)
    learn_times = models.IntegerField(verbose_name='学习时长',default=0)
    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name
        
class Video(BasicModel):
    lesson = models.ForeignKey(Lesson,verbose_name='章节名',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='视频名称',max_length=300)
    learn_times = models.IntegerField(verbose_name='学习时长',default=0)
    url = models.CharField(max_length=300,verbose_name='访问地址')
    
    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        
class CourseResource(BasicModel):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名称',max_length=300)
    file = models.FileField(verbose_name='封面图',upload_to='course/resourse/%Y/%m', max_length=200)
    
    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name