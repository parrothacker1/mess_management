from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Food
import json

# Create your views here.

@csrf_exempt #It's a threat but for practise i'm doing it
def food(request):
    if request.method=="POST":
        response={"success":True}
        data=json.loads(request.body)
        for i in data.keys():
            if i not in ['name','mess','reg_no']:
                response['success']=False
                break
        else:
            response['success']=True
        try:
            if (response['success']):
                d=Food(name=data['name'],mess=data['mess'],reg_no=data['reg_no'])
                d.save()
        except:
            response['success']=False
        return HttpResponse(json.dumps(response),status=200 if (response['success']) else 404)
    elif request.method=="GET":
        test=Food.objects.all()
        data_ret=[]
        for i in test:
            data_ret.append(i.get_details())
        return HttpResponse(json.dumps(data_ret),status=200)
    elif request.method=="PUT":
        response={'success':True}
        data=json.loads(request.body)
        for i in data.keys():
            if i not in ['name','mess','reg_no']:
                response['success']=False
                break
        else:
            response['success']=True
        try:
            if (response['success']):
                d=Food.objects.get(reg_no=data['reg_no'])
                d.name=data['name']
                d.mess=data['mess']
                d.save()
        except:
            response['success']=False
        return HttpResponse(json.dumps(response),status=200 if (response['success']) else 404)
    elif request.method=="DELETE":
        response={'success':True}
        data=json.loads(request.body)
        for i in data.keys():
            if i != "reg_no":
                response['success']=False
                break
        try:
            if (response['success']):
                d=Food.objects.get(reg_no=data['reg_no'])
                d.delete()
        except:
            response['success']=False
        return HttpResponse(json.dumps(response),status=200 if (response['success']) else 404)
    else:
        return HttpResponse("wrong http type")

