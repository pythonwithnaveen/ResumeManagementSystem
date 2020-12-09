from django.shortcuts import render,redirect
from process.forms import RegistrationForm
from process.models import RegistrationModel
from django.contrib.messages import success


def showIndex(request):
    return render(request,"process_templates/main.html")


def registration(request):
    print("===============1==============")
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        print("===============3==============")
        if rf.is_valid():
            print("===============4==============")
            rf.save()
            return redirect('user-otp')
        else:
            return render(request, 'process_templates/registration.html', {"form": rf})
    else:
        print("===============2==============")
        return render(request,'process_templates/registration.html',{"form":rf})


def userOTP(request):
    return render(request,"process_templates/otp.html")


def validate_otp(request):
    try:
        result = RegistrationModel.objects.get(contact=request.POST.get("t1"),otp=request.POST.get("t2"))
        if result.status == "pending":
            result.status = "approved" # updating
            result.save() # save
            success(request,"Thanks for Registration")
            return redirect('conformation')
        elif result.status == "approved":
            success(request, "Your Registration is Already Approved")
            return redirect('conformation')
        #elif result.status == "blocked":

    except RegistrationModel.DoesNotExist:
        message = "Sorry Invalid Details Please Try Again"
        return render(request,"process_templates/otp.html",{"message":message})



def conformation(request):
    return render(request,"process_templates/conformation.html")


def login(request):
    return render(request,'process_templates/login.html')


def login_check(request):
    try:
        result = RegistrationModel.objects.get(email=request.POST.get("u1"), password=request.POST.get("u2"))
        if result.status == "pending":
            return render(request, "process_templates/login.html", {"error": "Sorry Your Registration is not Approved"})
        if result.status == "closed":
            return render(request, "process_templates/login.html", {"error": "Sorry Your Account is Closed"})
        request.session["contact"] = result.contact
        request.session["name"] = result.name
        return redirect('view_profile')
    except RegistrationModel.DoesNotExist:
        return render(request,"process_templates/login.html",{"error":"Invalid User"})


def view_profile(request):
    return render(request,"process_templates/view_profile.html")


def logout(request):
    del request.session["contact"]
    del request.session["name"]
    return redirect('main_page')