from django.shortcuts import redirect, render

from UserApp.models import UserModel

# Create your views here.
def LoginView(request):
    if request.method=='POST':
        userData=UserModel.objects.get(email=request.POST['email'])
        if userData.password==request.POST['password']:
            request.session['userId']=userData.id
            return redirect('home')
    return render(request,'login.html');

def SignupView(request):
    if request.method=='POST':
        model=UserModel()
        model.name=request.POST['name']
        model.email=request.POST['email']
        model.contact=request.POST['number']
        model.password=request.POST['password']
        model.save()
        return redirect('login')
    return render(request,'signup.html');