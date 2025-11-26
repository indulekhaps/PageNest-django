from django.urls import path
from Adminapp import views

urlpatterns = [
    path('Index/', views.index, name="index"),
    path('Add_Book/', views.add_book, name="add_book"),
    path('Save_Book/', views.save_book, name="save_book"),
    path('Display_book/', views.display_book, name='display_book'),
    path('Edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('Update_book/<int:b_id>/', views.update_book, name='update_book'),
    path('Delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    path('add_category/', views.add_category, name="add_category"),
    path('save_Category/', views.save_category, name="save_category"),
    path('Display_Category/', views.display_category, name='display_category'),
    path('Edit_Category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('Update_Category/<int:c_id>/', views.update_category, name='update_category'),
    path('Delete_Category/<int:category_id>/', views.delete_category, name='delete_category'),

    path('Admin_login/', views.admin_login_page, name="admin_login_page"),
    path('Admin_login_auth/', views.admin_login, name="admin_login"),
    path('Admin_logout/', views.admin_logout, name="admin_logout"),

]
