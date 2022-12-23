from django.urls import path
from .  import views
app_name='ecomapp'
urlpatterns = [
    path('home/', views.allProdCat, name='allProdCat'),

    path('detail/<int:id>/', views.ProDetail, name='ProCatDetail'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('ahome/',views.admin_home, name='admin_home'),
    path('apps/',views.add_pro, name='add_pro'),
    path('delete/<int:pk>/',views.delete_pro,name="delete_pro"),
    path('update/<int:pk>/',views.update_pro,name='update_pro'),
    path('addprod/',views.add_pro,name="add_pro"),
    ]