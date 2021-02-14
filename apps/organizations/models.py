from django.db import models

from apps.users.models import BasicModel

category = (
    ('pxjg','培训机构'),
    ('gr','个人'),
    ('gx','高校')
)

class City(BasicModel):
    name = models.CharField(verbose_name='城市',max_length=100)
    desc = models.CharField(verbose_name='描述',max_length=300)
    
    class Meta:
        verbose_name='城市'
        verbose_name_plural = verbose_name
            
class CourseOrg(BasicModel):
    name = models.CharField(verbose_name='机构名称',max_length=50)
    desc = models.TextField(verbose_name='机构描述')
    tag = models.CharField(verbose_name='机构标签',max_length=10,default='世界知名')
    category = models.CharField(verbose_name='机构类别',max_length=10,default='pxjg',choices=category)
    click_nums = models.IntegerField(verbose_name='点击数',default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数',default=0)
    image = models.ImageField(verbose_name='logo', upload_to='org/%Y/%m',max_length=300)
    address = models.CharField(verbose_name='机构地址',max_length=300)
    students = models.IntegerField(verbose_name='学习人数',default=0)
    course_nums = models.IntegerField(verbose_name='课程数',default=0)
    city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='所属城市')
    
    class Meta:
        verbose_name='课程机构'
        verbose_name_plural = verbose_name
        
class Teacher(BasicModel):
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name='所属机构')
    name = models.CharField(verbose_name='教师名',max_length=50)
    work_years = models.IntegerField(verbose_name='工作年限',default=0)
    work_company = models.CharField(verbose_name='就职公司',max_length=100)
    work_position = models.CharField(verbose_name='公司职位',max_length=100)
    points = models.CharField(verbose_name='教学特点',max_length=100)
    click_nums = models.IntegerField(verbose_name='点击人数',default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数',default=0)
    age = models.IntegerField(verbose_name='年龄',default=18)
    image = models.ImageField(verbose_name='头像',upload_to='teacher/%Y/%m',max_length=300)
    
    class Meta:
        verbose_name='教师'
        verbose_name_plural = verbose_name