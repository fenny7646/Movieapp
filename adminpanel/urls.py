from django.urls import path,include
from . import views

app_name='adminpanel'

urlpatterns = [
    path('panel/', views.panel, name='panel'),
    path('adminmovies/', views.adminmovies, name='adminmovies'),
    #path('',views.,name='moviedetailer'),
    path('userlist/',views.userlist,name='userlist'),
    path('addmovie/',views.addmovie,name='addmovie'),
    path('userdelete/<int:user_id>',views.userdelete,name='userdelete'),
    #path('<slug:c_slug>/', views.allProdCat, name= 'movies_by_category'),
    #path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name= ''),
]