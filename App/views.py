from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital,UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from datetime import datetime




def base(request):
    return render(request,'App/base.html')

def index(request):
    data = Hospital.objects.all()
    return render(request, 'App/home.html',{'data':data})


def testCentres(request):
    return render(request,'App/test-centres.html')

def ctScan(request):
    return render(request,'App/ct-scan.html')

def ambulance(request):
    return render(request,'App/ambulance.html')

def helpLine(request):
    return render(request,'App/helpline.html')


def basicprofile(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        two = request.POST.get('two')
        to = request.POST.get('to')
        twv = request.POST.get('twv')
        tv = request.POST.get('tv')


        # my_data = total(name = name,total_beds_with_oxygen=to,total_beds_without_oxygen=two,total_icu_with_ventilator=tv,total_normal_icu=twv)
        # my_data.save()

        messages.success(request,'Your Bed Information is updated')

    return render(request,'App/profile.html')


# total_beds_with_oxygen = models.IntegerField(null=True)
#     total_beds_without_oxygen = models.IntegerField(null=True)
#     total_icu_with_ventilator = models.IntegerField(null=True)
#     total_normal_icu = models.IntegerField(null=True)


def adminPanel(request):
    data = Hospital.objects.filter(name = request.user)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if(request.method == 'POST'):
        name = request.user
        bwo = request.POST.get('bwo','')
        bwoo = request.POST.get('bwoo','')
        wv = request.POST.get('wv','')
        wov = request.POST.get('wov','')
        two = request.POST.get('two')
        to = request.POST.get('to')
        twv = request.POST.get('twv')
        tv = request.POST.get('tv')
        time_stamp = current_time

        phone = request.POST.get('phone','')
        address = request.POST.get('address','')


        saveData = Hospital(phone=phone,address=address,name=name,beds_with_oxygen=bwo,beds_without_oxygen=bwoo,icu_with_ventilator=wv,normal_icu=wov,
                            total_beds_with_oxygen=to,total_beds_without_oxygen=two,total_icu_with_ventilator=tv,total_normal_icu=twv,
                            time_update=time_stamp)

        if(data):
            Hospital.objects.filter(name = request.user).update(name=name,beds_with_oxygen=bwo,beds_without_oxygen=bwoo,icu_with_ventilator=wv,normal_icu=wov,
                                total_beds_with_oxygen=to,total_beds_without_oxygen=two,total_icu_with_ventilator=tv,total_normal_icu=twv,
                                time_update=time_stamp)
            messages.success(request, 'Data Updated Successfully')
        else:
            saveData.save()
            messages.success(request,'Congratulations! Your data has been uploaded')





    return render(request,'AdminPanel/adminHome.html',{'data':data})



def base2(request):
    return render(request,'App/base2.html')


def signin(request):
    if(request.method == "POST"):
        name = request.POST.get('name','')
        passw = request.POST.get('pass','')
        user = authenticate(username=name, password=passw)
        login(request,user)
        return redirect(adminPanel)
    return render(request,'App/login.html')

def signup(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['p1']
        pass2 = request.POST['p2']


        getData = User.objects.filter(username = name)
        print(getData)
        if(getData):
            messages.warning(request,'User Already Registered')
        else:
            myuser = User.objects.create_user(name, email, pass1)
            myuser.first_name = name
            myuser.save()
            messages.success(request,'You have successfully registered')

            user  = authenticate(username = name,password = pass1)
            if user is not None:
                login(request,user)
                messages.success(request, 'You have successfully registered')
                return redirect(adminPanel)

            else:
                messages.success(request, 'Something wrong :( Registration failed')

    return render(request,'App/signup.html',)

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect(index)