from django.urls import path
from Webapp import views

urlpatterns=[
    path('Home/', views.home, name="home"),
    path('About/', views.about, name="about"),
    path('Contact/', views.contact, name="contact"),
    path('Save_Contact/', views.save_contact, name="save_contact"),
    path('View_Contact/', views.view_contact, name="view_contact"),
    path('Delete_Contact/<int:books_id>/', views.delete_contact, name="delete_contact"),
    path('Popular_Books/', views.popular_books, name="popular_books"),
    path('Checkout/', views.checkout, name="checkout"),
    path('Cart/', views.cart, name="cart"),
    path('Save_Cart/', views.save_cart, name="save_cart"),
    path('Filtered_Books/<str:book_category>/', views.filtered_books, name='filtered_books'),
    path('Single_Book/<int:booksingle_id>/', views.single_book, name='single_book'),
    path('Sign_in/', views.sign_in, name="sign_in"),
    path('Sign_up/', views.sign_up, name="sign_up"),
    path('Save_sign_up/', views.save_sign_up, name="save_sign_up"),
    path('Save_Sign_in/', views.save_sign_in, name="save_sign_in"),
    path('Logout/', views.logout, name="logout"),

]