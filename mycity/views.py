from django.contrib.auth.models import User
from django.http import Http404
from mycity.serializers import UserSerializer, OTPSerializer, OTPOTPSerializer, CityTrackerSerializer, CityListSerializer, IssueListSerializer
from mycity.models import OTP, MyCity, CityList, IssueList
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OTPView(APIView):
    def post(self, request, format=None):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, phone, format=None):
        try:
            otps = OTP.objects.get(pk=phone)
            serializer = OTPOTPSerializer(otps)
            return Response(serializer.data)#instead send SMS to otps.phone with otps.otp
        except OTP.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, phone, rcdotp, format=None):
        try:
            otps = OTP.objects.get(pk=phone, otp=rcdotp)
            serializer = OTPOTPSerializer(otps, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("verified",status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except OTP.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class IWillTrack(APIView):
    def post(self, request, format=None):
        serializer = CityTrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

#    def get(self, request, format=None):
#        trackers = MyCity.objects.all()
#        serializer = CityTrackerSerializer(trackers, many=True)
#        return Response(serializer.data)

#def MyTracker(request):
#    filter=CityTrackerSerializer(MyCity.objects.filter(date__year=2016),many=True)
#    return render(request, 'mycity.html', {'filter': filter})

class CityOverView(APIView):
    def get(self,request,category,fdate,tdate,format=None):
        gps = MyCity.objects.filter(category=category,timestamp__gte=fdate,timestamp__lte=tdate)
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
