from django.shortcuts import render,redirect
from Adminapp.models import Category,Bookdb
from Webapp.models import contactdb,Registerdb


# Create your views here.
def home(request):
    categories=Category.objects.all()
    books = Bookdb.objects.all()
    return render(request,"Home.html",{
        'categories': categories,
        'books': books
    })
def about(request):
    categories = Category.objects.all()
    return render(request,"About.html",{
        'categories': categories})
def contact(request):
    return render(request,"Contact.html")
def save_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('subject')
        mess=request.POST.get('message')
        obj= contactdb(Name=name,Email=email,Subject=sub,Message=mess)
        obj.save()
        return redirect(contact)

def view_contact(request):
    data=contactdb.objects.all()
    return render(request, "View_Contact.html",{'data':data})
def delete_contact(request,books_id):
    data = contactdb.objects.filter(id=books_id)
    data.delete()
    return redirect(view_contact)


def popular_books(request):
    categories = Category.objects.all()
    books=Bookdb.objects.all()
    return render(request, "Popular_Books.html", {
        'categories': categories,
        'books': books
    })
def checkout(request):
    return render(request,"Checkout.html")

def cart(request):
    return render(request,"Cart.html")
def filtered_books(request, book_category):
    categories = Category.objects.all()
    books = Bookdb.objects.filter(Category_name=book_category)
    return render(request, "Filtered_Books.html",{
        'categories': categories,
        'books': books
    })

def single_book(request,booksingle_id):
    book=Bookdb.objects.get(id=booksingle_id)
    return render(request, "Single_Book.html",{'book': book})



def sign_in(request):
    return render(request,"Sign_In.html")
def sign_up(request):
    return render(request,"Sign_Up.html")

def save_sign_up(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        pwd=request.POST.get('pass')
        cpwd=request.POST.get('re_pass')
        obj=Registerdb(Username=name,Password=pwd,Email=email,Conf_password=cpwd)
        obj.save()
        return redirect(sign_up)

def save_sign_in(request):
    if request.method=="POST":
        un=request.POST.get('your_name')
        pswd=request.POST.get('your_pass')
        if Registerdb.objects.filter( Username=un,Password=pswd).exists():
            request.session['Username']=un
            request.session['Password']=pswd
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        return  redirect(sign_in)

def logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home)