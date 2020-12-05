from django.shortcuts import render,redirect
from process.forms import RegistrationForm


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