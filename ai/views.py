from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics, status, filters

from urllib import request as rqt
from io import BytesIO
from PIL import Image
from .import load
import json
import requests


# from django.utils import timezone

# AI 이미지 분석을 통한 결과 저장
# 만든이 : snchoi
@api_view(['GET'])
def AiImgGrocery(request):
    #------------근웅----------------
    url = "https://themightiestkpk1.s3.amazonaws.com/train12124.jpg"
    # url = 'https://themightiestkpk1.s3.amazonaws.com/test9.jpg'
    # model_path = 'ai/000/trained_weights_final.h5'
    # class_path = 'ai/_classes.txt'

    # yolo = YOLO(model_path=model_path, classes_path=class_path)

    # 이미지 로딩
    res = rqt.urlopen(url).read()
    img = Image.open(BytesIO(res))
    ai_result = load.pre_yolo.yolo.my_detect_image(img)

    # ------------------------------
    return JsonResponse(ai_result, safe=False)

  
# AI 이미지 분석을 통한 결과 저장 복사본
# 만든이 : snchoi
@api_view(['GET'])
def AITest(request):
    # 이미지 정보 받음
    url = request.GET.get('url')
    print('url : ', url)

    #------------근웅----------------
    # url = "https://themightiestkpk1.s3.amazonaws.com/train12124.jpg"
    # url = 'https://themightiestkpk1.s3.amazonaws.com/test9.jpg'
    # model_path = 'ai/000/trained_weights_final.h5'
    # class_path = 'ai/_classes.txt'

    # yolo = YOLO(model_path=model_path, classes_path=class_path)

    # 이미지 로딩
    res = rqt.urlopen(url).read()
    img = Image.open(BytesIO(res))
    ai_result = load.pre_yolo.yolo.my_detect_image(img)

    # ------------------------------

    # AI분석 로직
    # ai_result = [{
    #     'all_grocery_id': 1,
    #     'name' : '바나나',
    #     'count' : 3,
    #     'coordinate' : [[1,2],[3,2]]
    # },{
    #     'all_grocery_id': 2,
    #     'name' : '사과',
    #     'count' : 1,
    #     'coordinate' : [[1,2],[3,2]]
    # },{
    #     'all_grocery_id': 3,
    #     'name' : '고구마',
    #     'count' : 2,
    #     'coordinate' : [[1,2],[3,2]]
    # }]

    print('타입 : ', type(ai_result))
    print('ai_result : ', ai_result)
    
    # ai_result = json.dumps(ai_result)
    # print('타입 : ', type(ai_result))
    # ai_result = json.loads(ai_result)
    # print('타입 : ', type(ai_result))
    return Response(ai_result)

        

