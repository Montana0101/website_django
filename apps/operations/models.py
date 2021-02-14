from django.db import models

from apps.users.modles import BasicModel
from apps.courses.modles import Course
from django.contrib.auth import get_user_model

user_profile = get_user_model()
#收藏枚举
fav_types = (
    (1,'课程'),
    (2,'课程机构'),
    (3,'讲师')
)

class UserAsk(BasicModel):
    name = models.CharField(verbose_name='姓名',max_length=100)
    mobile = models.IntegerField(verbose_name='手机',max_length=11)
    course_name = models.CharField(verbose_name='课程名',max_length=50)

    class Meta:
        verbose_name='用户咨询'
        verbose_name_plural = verbose_name

# 课程评论
class CourseComments(BasicModel):
    user = models.ForeignKey(user_profile,verbose_name='用户')
    course = models.ForeignKey(Course,verbose_name='课程')
    comments = models.TextField(verbose_name='评论内容')
    
    class Meta:
        verbose_name='课程评论'
        verbose_name_plural = verbose_name

# 收藏
class UserFavourite(BasicModel):
    user = models.ForeignKey(user_profile,verbose_name='用户')
    fav_id = models.IntegerField(verbose_name='数据id')
    fav_type = models.IntegerField(verbose_name='收藏类型',choices=fav_types,default=1)
    
    class Meta:
        verbose_name='用户收藏'
        verbose_name_plural = verbose_name

# 用户消息
class UserMessage(BasicModel):
    user = models.ForeignKey(user_profile,verbose_name='用户')
    message = models.CharField(verbose_name='消息内容',max_length=500)
    has_read = models.BooleanField(verbose_name='是否已读',default=False)
    
    class Meta:
        verbose_name='用户消息'
        verbose_name_plural=verbose_name
    
# 用户课程
class UserCourse(BasicModel):
    user = models.ForeignKey(user_profile,verbose_name='用户')
    course = models.ForeignKey(Course,verbose_name='课程')
    
    class Meta:
        verbose_name='用户课程'
        verbose_name_plural=verbose_name