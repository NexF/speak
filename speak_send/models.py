from operator import mod
from django.db import models

USER_ID_MAX = 16*1024*1024*1024         # 最大支持16b的用户数
GRUP_ID_MIN = USER_ID_MAX + 1           # 用户数之后就是群聊数

# 定义消息消息可派生出音视图文等
# 可以从mid唯一确定一条消息
class Message(models.Model):
    mid = models.BigIntegerField()                                               # 定义消息ID（群）
    send_tid = models.BigIntegerField()                                          # 定义消息的发送用户
    recv_tid = models.BigIntegerField()                                          # 定义消息的接收用户（群）
    send_date = models.DateTimeField('msg published')                                       # 定义消息发送时间
    type = models.IntegerField()                                                 # msgtype = 0:text,1:pic,2:audio,3:video,4:file
    text = models.CharField(max_length=4096)
    url = models.CharField(max_length=1024)
    def __str__(self):
        desp = ""
        if self.msg_type == 0:
            desp = self.text
        else:
            desp = self.url
        return "mid=%d,type=%d,desp=%s"%(self.mid,self.type,desp)

# 发送/接收消息的目标，可以是人也可以是群
class MsgTarget(models.Model):
    tid = models.BigIntegerField()                  # 目标id
    name = models.CharField(max_length=64)          # 目标名称
    head_pic = models.CharField(max_length=1024)    # 头像url

# Target下的接收消息目标，用于群发消息
class SubTarget(models.Model):
    msgtarget = models.ForeignKey("MsgTarget", on_delete=models.CASCADE)    # 外键，关联MsgTarget
    tid = models.BigIntegerField()                  # 目标id