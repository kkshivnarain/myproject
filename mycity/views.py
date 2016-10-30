from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import Http404
from mycity.serializers import UserSerializer, OTPSerializer, OTPOTPSerializer, CityTrackerSerializer, CityListSerializer, IssueListSerializer, UserCreditSerializer
from mycity.models import OTP, MyCity, CityList, IssueList, UserCredit, UserCreditDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import random,string,base64
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def newpwd():
    password=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return password

class OTPView(APIView):
    def post(self, request, format=None):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.create(username=serializer.data['phone'],
                                     first_name=serializer.data['first_name'],
                                      password=newpwd())
            mypassword=user.password
            user.set_password(user.password)
            user.save()
            usercredit=UserCredit.objects.create(userid=serializer.data['phone'])
            usercredit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, phone, format=None):
        try:
            otps = OTP.objects.get(pk=phone)
            serializer = OTPOTPSerializer(otps)
            return Response("SMS Sent on your Mobile Number")#instead send SMS to otps.phone with otps.otp
        except OTP.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, phone, rcdotp, format=None):
        try:
            otps = OTP.objects.get(pk=phone, otp=rcdotp)
            serializer = OTPOTPSerializer(otps, data=request.data)
            if serializer.is_valid():
                serializer.save()
                user=User.objects.get(username=phone)
                newpassword=newpwd()
                user.set_password(newpassword)
                user.save()
                auth="Basic "+base64.standard_b64encode(phone+":"+newpassword)
                #send password info to ajax
                return Response(auth,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except OTP.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class IWillTrack(APIView):
#    authentication_classes = (BasicAuthentication,)
#    permission_classes = (IsAuthenticated,)
    def post(self, request, phone, format=None):
        serializer = CityTrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            credit=UserCreditDetails.objects.create(userid=phone)
            credit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class CityOverView(APIView):
    def get(self,request,city,category,fdate,tdate,format=None):
        gps = MyCity.objects.filter(timestamp__gte=fdate, timestamp__lte=tdate, category=category,city=city)
        serializer = CityTrackerSerializer(gps, many=True)
        return Response(serializer.data)

class CityListView(APIView):
    def get(self, request, format=None):
        try:
            city = CityList.objects.all()
            serializer = CityListSerializer(city,many=True)
            return Response(serializer.data)
        except CityList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class IssueListView(APIView):
    def get(self, request, format=None):
        try:
            city = IssueList.objects.all()
            serializer = IssueListSerializer(city,many=True)
            return Response(serializer.data)
        except IssueList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


#@login_required
def Index(request):
    citylist=CityList.objects.all()
    issuelist=IssueList.objects.all()
    return render(request, "mycity.html",{'citylist':citylist,'issuelist':issuelist})

class Coordinates(APIView):
    def get(self, request,city, format=None):
        try:
            city = CityList.objects.filter(city=city)
            serializer = CityListSerializer(city,many=True)
            return Response(serializer.data)
        except CityList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

#20160905 add this to core and also change serializer to 
class LoginView(APIView):
    authentication_classes = (BasicAuthentication,)
    serializer_class = UserSerializer
 
    def post(self, request, *args, **kwargs):
        return Response("Authenticated")
    

class AuthView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response("Authenticated")
#        return Response(UserSerializer(request.user).data)
 
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UserCreditView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,) 
    def get(self, request,phone, format=None):
        try:
            credit = UserCredit.objects.get(userid=phone)
            credit.weekscore(0)
            credit.weekscore(1)
            credit.save()
            serializer = UserCreditSerializer(credit)
            return Response(serializer.data)
        except UserCredit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

