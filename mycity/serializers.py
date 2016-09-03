from django.contrib.auth.models import User
from mycity.models import OTP, MyCity, CityList, IssueList
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
            
        
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('phone',)


class OTPOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('otp',)

class CityTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCity
        fields = ('category','latitude','longitude','timestamp','city')

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityList
        fields = ('city',)

class IssueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueList
        fields = ('category','category_desc',)
