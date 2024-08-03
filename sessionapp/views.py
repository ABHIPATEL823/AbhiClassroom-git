from django.shortcuts import render,redirect
from datetime import datetime,timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from icecream import ic


# Create your views here.

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"message": "Hello, world!"})

def my_cookies(request):
    response = redirect('get_cookies')
    expires = datetime.now() + timedelta(minutes=2)
    response.set_cookie(key="name1",value="anurag1",secure=True,max_age=2*60)
    return response

def get_cookies(request):
    name = request.COOKIES["name1"]
    return render(request,'home.html',{"name":name})

def delete_cookies(request):
    response = redirect('get_cookies')
    response.delete_cookie("name1")
    return response