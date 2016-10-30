from django.contrib import admin
from mycity.models import OTP, MyCity, CityList, IssueList, UserCredit, UserCreditDetails

# Register your models here.
@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display=('phone','otp','verified')

@admin.register(MyCity)
class MyCityAdmin(admin.ModelAdmin):
    list_display=('city','category','timestamp')

@admin.register(CityList)
class CityListAdmin(admin.ModelAdmin):
    list_display=('city',)
    
@admin.register(IssueList)
class IssueListAdmin(admin.ModelAdmin):
    list_display=('category','category_desc')
    
@admin.register(UserCredit)
class IssueListAdmin(admin.ModelAdmin):
    list_display=('userid','credit')

@admin.register(UserCreditDetails)
class IssueListAdmin(admin.ModelAdmin):
    list_display=('userid','created_date')