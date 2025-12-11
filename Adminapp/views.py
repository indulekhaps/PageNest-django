from django.shortcuts import render,redirect
from Adminapp.models import Category,Bookdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index(request):
    categoriesnum=Category.objects.count()
    booknum=Bookdb.objects.count()
    date=datetime.datetime.now()
    return render(request,"index.html",{'categoriesnum':categoriesnum ,'booknum':booknum ,
                                        'date':date})

def add_category(request):
    return render(request,"Add_categories.html")
def save_category(request):
    if request.method == "POST":
        c_name=request.POST.get('Category_name')
        c_desc=request.POST.get('description')
        c_img=request.FILES['cover_image']
        obj=Category(Category_name=c_name,Description=c_desc,Cover_img=c_img)
        obj.save()
        messages.success(request,"Category saved Successfully..!")
        return redirect(add_category)
def display_category(request):
    data=Category.objects.all()
    return render(request,"Display_categories.html",{'data':data})
def edit_category(request,category_id):
    category=Category.objects.get(id=category_id)
    return render(request, "Edit_category.html",{'category':category})

def update_category(request,c_id):
    if request.method == "POST":
        c_name = request.POST.get('Category_name')
        c_desc = request.POST.get('description')
        try:
             c_img = request.FILES['cover_image']
             fs=FileSystemStorage()
             file=fs.save(c_img.name,c_img)

        except MultiValueDictKeyError:
            file=Category.objects.get(id=c_id).Cover_img
        Category.objects.filter(id=c_id).update(Category_name=c_name,Description=c_desc,Cover_img=file)
        return redirect(display_category)

def delete_category(request,category_id):
    data = Category.objects.filter(id=category_id)
    data.delete()
    return redirect(display_category)

def add_book(request):
    categories=Category.objects.all()
    return render(request,"Add_Book.html",{'categories':categories})

def save_book(request):
    if request.method == "POST":
        b_name=request.POST.get('book_title')
        b_author=request.POST.get('author')
        b_category=request.POST.get('category')
        b_desc=request.POST.get('description')
        b_publisher=request.POST.get('publisher')
        b_price=request.POST.get('price')
        b_pic=request.FILES['cover_image']
        obj=Bookdb(Book_name= b_name,Author=b_author,Category=b_category,Publisher=b_publisher,Description=b_desc,Price=b_price,Cover_pic=b_pic)
        obj.save()
        return redirect(add_book)

def display_book(request):
    data=Bookdb.objects.all()
    return render(request,"Display_book.html",{'data':data})

def edit_book(request,book_id):
    Book=Bookdb.objects.get(id=book_id)
    categories=Category.objects.all()
    return render(request,"Edit_book.html",{'Book':Book ,'categories':categories})

def update_book(request,b_id):
    if request.method == "POST":
        b_name=request.POST.get('book_title')
        b_author=request.POST.get('author')
        b_category=request.POST.get('category')
        b_desc=request.POST.get('description')
        b_publisher=request.POST.get('publisher')
        b_price=request.POST.get('price')

        try:
             b_pic = request.FILES['cover_image']
             fs=FileSystemStorage()
             file=fs.save(b_pic.name,b_pic)

        except MultiValueDictKeyError:
            file=Bookdb.objects.get(id=b_id).Cover_pic
        Bookdb.objects.filter(id=b_id).update(Book_name= b_name,Author=b_author,Category=b_category,Publisher=b_publisher,Description=b_desc,Price=b_price,Cover_pic=file)
        return redirect(display_book)

def delete_book(request,book_id):
    data=Bookdb.objects.filter(id=book_id)
    data.delete()
    return redirect(display_book)

def admin_login_page(request):
    return render(request,"Admin_Login.html")

def admin_login(request):
    if request.method == "POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data=authenticate(username=un,password=pwd)
            if data is not None:
                login(request,data)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(index)
            else:
                return redirect(index)
        else:
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)
