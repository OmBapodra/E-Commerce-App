from django.shortcuts import redirect, render

from ProductApp.models import CatagoryModel, ProductModel

# Create your views here.
def HomeView(request):
    if 'userId' in request.session.keys():
        catagoryData=CatagoryModel.objects.all()
        print(catagoryData)
        return render(request,'home.html',{'catagoryData' : catagoryData});
    else:
        return redirect('login')

def ProductView(request):
    if 'userId' in request.session.keys():
        productData=ProductModel.objects.all()
        return render(request,'product.html',{'productData':productData});
    else:
        return redirect('login')

def LogoutView(request):
    del request.session['userId']
    return redirect('login')