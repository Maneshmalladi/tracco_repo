from django.shortcuts import render,redirect

# Create your views here.

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.contrib import messages
# Create your views here.

from testapp.models  import RegModel

def start_page(request):
    return render(request,'testapp/start.html')

def  signup_view(request):
    if request.method=='POST':
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        em=request.POST.get('email')
        gen=request.POST.get('sex')
        pas=request.POST.get('password')
        rpas=request.POST.get('conf_password')

        if RegModel.objects.filter(email=em):
            messages.error(request,"Email already exits ")
            #return HttpResponse("already undhi eni sarluu rasthavuu raa kuyyayaa")
            return render(request, "testapp/signup.html")

        if pas != rpas:
            messages.error(request,'Password must  should be same ')
            return render(request,"testapp/signup.html")

        elif em[-10:]!='@gmail.com':
            messages.error(request, 'Email should end in @gmail.com')
            return render(request, "testapp/signup.html")


        else:
            RegModel.objects.create(fname=fn, lname=ln, email=em, gender=gen, password=pas, rpassword=rpas)
            messages.success(request,"Signup Successfully created please LogIn!!..")
            return render(request,'testapp/login.html')


        #RegModel.objects.create(fname=fn,lname=ln,email=em,gender=gen,password=pas,rpassword=rpas)



    return  render( request,'testapp/signup.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = RegModel.objects.get(email=email, password=password)
            return render(request, "testapp/MarriageInv.html")
        except RegModel.DoesNotExist:
            messages.error(request, 'Account is not Exist Create New Account')
            return render(request, "testapp/login.html")

           # return render(request,'testapp/signup.html')
    return render(request, "testapp/login.html")



def forgot_view(request):

    if request.method=='POST':
        user_id=request.POST.get('email')
        #forget = RegModel.objects.get(email=user_id)
        try:
            forget = RegModel.objects.get(email=user_id)
        except RegModel.DoesNotExist:
            messages.error(request,"User with the provided email does not exist.")
            return render(request,'testapp/forget.html')

        forget.email = request.POST.get('email')
        forget.password = request.POST.get('password')
        forget.rpassword = request.POST.get('conf_password')

        if forget.password != forget.rpassword:
            messages.error(request,'Password must  should be same ')
            return render(request,"testapp/forget.html")
        forget.save()

        return render(request,'testapp/login.html')
    return render(request,'testapp/forget.html')



def recp_page(request):
    return render(request,'testapp/Recp1.html')

def groom_page(request):
    return render(request,'testapp/Groom1.html')

def bride_page(request):
    return render(request,'testapp/Bride1.html')


def invite_page(request):
    return render(request,'testapp/MarriageInv.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

#{% url 'log' %}


def about_view(request):
    return render(request, 'testapp/About.html')
