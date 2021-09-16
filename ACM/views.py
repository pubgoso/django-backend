from os import error
from django.db.models.fields import DateField
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view
import json
from django.core import serializers
from django.db import transaction
from .untils import MyResponse
import time
# Create your views here.


@api_view(['GET'])
def get_info(request):
    All = Info.objects.all()

    return MyResponse(
        data = All.values(),
        status=200,
        msg='获取版本信息成功'
    )



@api_view(['POST'])
def login(request):

    userName = request.data.get('username')
    password = request.data.get('password')
    # check_ = 
    temp = Alluser.objects.filter(username=userName)

    if not temp:
        return MyResponse(
            status=500,
            msg='用户名错误',
        )
    now_user = temp.values()[0]
    if  now_user["password"] != password:
        return MyResponse(
            status=500,
            msg='密码错误'
        )

    _type  = Alluser.objects.get(username = userName).type

    dataForm = {}
    for item in now_user:
        dataForm[item]=now_user[item]

    if _type == 1:
        dataForm["id"] = Root.objects.get(username=userName).id

    if _type == 2:
        dataForm["id"] = Mentor.objects.get(username=userName).id

    if _type == 3:
        dataForm["id"] = User.objects.get(username=userName).id

    dataForm["type"] = _type
    return MyResponse(
        data=dataForm,
        status=200,
        msg='登陆成功'
    )
    
    
@api_view(['POST'])
def addStudent(request):
    username = request.data.get('userName')
    if len(Alluser.objects.filter(username=username)) != 0:
        return MyResponse(
            status=500,
            msg='用户名不可用'
        )
    password = request.data.get('password')
    name = request.data.get('name')
    class_field = request.data.get('class_field')
    mid_id = request.data.get('mid_id')
    with transaction.atomic():
        Alluser.objects.create(name=name,username=username,password=password,type=3)
        User.objects.create(name=name,username=username,password=password,class_field=class_field,mid=Mentor.objects.get(id=mid_id))
        return MyResponse(
            msg='添加成功',
            status=200
        )
    return MyResponse(
        status=500,
        msg='错误'
    )


@api_view(['POST'])
def addMentor(request):
    username = request.data.get('userName')
    if len(Alluser.objects.filter(username=username)) != 0:
        return MyResponse(
            status=500,
            msg='用户名不可用'
        )
    password = request.data.get('password')
    name = request.data.get('name')

    print(username)
    with transaction.atomic():
        Alluser.objects.create(name=name,username=username,password=password,type=2)
        Mentor.objects.create(name=name,username=username,password=password)
        return MyResponse(
            msg='添加成功',
            status=200
        )
    print('nowwd')
    return MyResponse(
        status=500,
        msg='错误'
    )


@api_view(['GET'])
def studentList(request):
    All= User.objects.all().order_by('-score')
    # for item in All:
    #     print('ddd=',item.Mentor)
    return MyResponse(
        data=All.values(),
        status=200,
        msg='获取学生列表成功'
    )


@api_view(['GET'])
def mentorList(request):
    All= Mentor.objects.all()
    return MyResponse(
        data=All.values(),
        status=200,
        msg='获取mentor信息成功'
    )


@api_view(['POST'])
def updateUser(request):
    id = request.data.get('id')
    mentor_id = request.data.get('mid_id')
    password = request.data.get('password')
    data = User.objects.get(id=id)
    data.mid_id = mentor_id
    data.password = password
    data.save()
    return MyResponse(
        status=200,
        msg='mentor成功指定'
    )


@api_view(['POST'])
def addQuestion(request):
    link = request.data.get('link')
    score = request.data.get('score')
    info = request.data.get('info')
    end_time = request.data.get('end_time')
    now_time = time.strftime("%Y-%m-%d", time.localtime()) 
    Question.objects.create(link=link,info=info,start_time=now_time,end_time=end_time,score=score)
    return MyResponse(
        status=200
    )


@api_view(['GET'])
def questionList(request):
    All= Question.objects.all()
    return MyResponse(
        data=All.values(),
        status=200,
        msg='获取question成功'
    )


@api_view(['POST'])
def updateQuestion(request):
    params = request.data
    print('params=',params)
    Alink = params.get('Alink');
    qid = params.get('qid');
    question = Question.objects.get(id=qid)

    uid = params.get('uid');
    student = User.objects.get(id=uid)
    Submissions.objects.create(question=question,student=student,alink=Alink,status=10,time=time.strftime("%Y-%m-%d %H:%M", time.localtime()))
    return MyResponse(
        status=200
    )


@api_view(['GET'])
def getAuditLog(request):
    All = Auditlog.objects.all()
    data = []
    for item in All:
        print(item)
        data.append({
            "id":item.stu.id,
            "mentor_id":item.mentor.id,
            "question_id":item.question.id,
            "time_log":item.time_log,
            "status":item.status
        })    
    return MyResponse(
        data=data,
        status=200,
        msg='获取审核日志成功'
    )


@api_view(['GET'])
def getSubmissions(request):
    id = request.query_params.get('id')
    All = Submissions.objects.filter(student=id)
    Data = []
    for item in All:
        temp ={
            "id":item.id,
            "time":item.time,
            "info":item.question.info,
            "qlink":item.question.link,
            "alink":item.alink,
            "score":item.question.score,
            "status":item.status
        }
        Data.append(temp)
    return MyResponse(
        data=Data,
        status=200,
        msg='获取提交信息成功'
    )


@api_view(['GET'])
def getPendingJudgeList(request):
    # 找到mentor是id的所有人的status为10的 submission
    id = request.query_params.get('id')

    All = []

    Data = Submissions.objects.filter(status=10)

    for item in Data:
        if item.student.mid.id == int(id):
            temp = {
                "id":item.id,
                "name":item.student.name,
                "qlink":item.question.link,
                "alink":item.alink,
                "end_time":item.question.end_time,
                "score":item.question.score
            }
            All.append(temp)
    
    return MyResponse(
        data=All,
        status=200,
        msg='获取待审核提交成功'
    )

@api_view(["POST"])
def updateSubmission(request):
    # 该操作 为 通过 or 拒绝 
    id = request.data.get('id');
    status = request.data.get('status');

    Submissions.objects.filter(id=id).update(status=status);
    # 20 ac  30 wa 
    if int(status) == 20:
        temp = Submissions.objects.get(id=id)
        sid = temp.student.id
        q = temp.question
        print('id=',sid,q.score)
        with transaction.atomic():
            Auditlog.objects.create(stu=temp.student,
            mentor=temp.student.mid,question=q,status=int(status),time_log=time.strftime("%Y-%m-%d", time.localtime()))
            # print('len=',Aclog.objects.filter(student=sid).get(id) )
            if len(Aclog.objects.filter(student=sid,question=q.id)) == 0:
                Aclog.objects.create(
                    question=Question.objects.get(id=q.id),
                    student=User.objects.get(id=sid),
                    time=time.strftime("%Y-%m-%d %H:%M", time.localtime()))
                tempt= User.objects.get(id=sid)
                print('ttt',tempt)
                tempt.score+=q.score
                tempt.save()
    return MyResponse(
        status=200,
        msg='操作成功'
    )