from django.core.paginator import Paginator ,InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import  Product
from django.contrib import messages, auth
from django.contrib.auth.models import User
from . forms import ProductForm



# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("ecomapp:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect("ecomapp:register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect("ecomapp:register")
        return redirect("ecomapp:login")
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user and user.is_superuser==True:
            auth.login(request,user)
            return redirect('ecomapp:admin_home')
        elif user and user.is_superuser==False:
            auth.login(request,user)
            return redirect('ecomapp:allProdCat')
        else:
            messages.info(request,"invalid credentials")
            return redirect("ecomapp:login")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("ecomapp:login")


def  add_pro(request,):

    form=ProductForm()

    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('ecomapp:admin_home')
    return render(request, 'add_product.html', {'form': form})



def admin_home(request):
	pro_d=Product.objects.all()
	return render(request,'admin_view.html',{"prod":pro_d})


def delete_pro(request, pk):
    b = Product.objects.get(pk=pk)
    b.delete()

    return admin_home(request)

def update_pro(request,pk):
    prodd=Product.objects.get(pk=pk)
    f=ProductForm(request.POST or None,request.FILES , instance=prodd)
    if f.is_valid():
        f.save()
        return redirect('ecomapp:admin_home')
    return render(request,'update.html',{'f':f,'prodd':prodd})

def allProdCat(request,):
    c_page = None

    products_list = Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page', '1'))
    except:
        page= 1
    try:
        products=paginator.page(page)
    except  (InvalidPage, EmptyPage):
        products= paginator.page(paginator.num_pages)


    return render(request, "category.html", {'category': c_page, 'products': products})


def  ProDetail(request,id):
    try:
        product = Product.objects.get(id=id)
    except  Exception as e:
        raise e
    return render(request, "product.html", {'product': product})


