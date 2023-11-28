from django.shortcuts import render,redirect
from .models import contact

# Create your views here.
def index(request):
    if request.POST:
        uname=request.POST.get('username')
        email=request.POST.get('email')
        address=request.POST.get('address')
        number=request.POST.get('number')
        date=request.POST.get('datetime')
        msg=request.POST.get('message')
        data=""
        try:
            if len(number)==10:
                details=contact(uname=uname,email=email,address=address,phone=str(number),datetime=date,message=msg)
                details.save()
                data="Message Sented!"
                er={'data':data}
                return render(request,"index.html",er)
            else:
                data="Mobile number is invalid"
                er={'data':data}
                return render(request,"index.html",er)
        except:
            data="Message was not sented error occured"
            er={'data':data}
            return render(request,"index.html",er)


    return render(request,'index.html')
