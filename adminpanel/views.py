from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
#from main.models import Category, Movies
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def panel(request):
    return render(request, 'panel/panel_main.html')

def adminmovies(request):
    return render(request, 'panel/panel_acc_setting.html')

def userlist(request):
    users = User.objects.all()
    return render(request, 'panel/panel_user_list.html',{'users':users})

def addmovie(request):
    return render(request, 'panel/panel_acc_form_add.html')
    
def userdelete(request, user_id):    
   if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('adminpanel:userlist')
   else:
        return HttpResponseNotAllowed(['POST'])




# def allMovCat(request, c_slug= None):
#     c_page= None
#     movie_list= None
#     if c_slug != None:
#         c_page = get_object_or_404(Category, slug= c_slug)
#         movie_list = Movies.objects.all().filter( category= c_page, available = True )
#     else:
#         movie_list = Movies.objects.all().filter( available= True)
#     paginator= Paginator(movie_list, 6)
#     try:
#         page= int(request.GET.get('page', '1'))
#     except:
#         page= 1
#     try:
#         movies= paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         movies= paginator.page(paginator.num_pages)
    
#     return render(request, "category.html", { 'category':c_page, 'movies': movies})
    
# def movDetail(request, c_slug, movie_slug):
#     try:
#         movie= Movies.objects.get(category__slug= c_slug, slug= movie_slug)
#     except Exception as e:
#         raise e
#     return render(request, 'product.html', {'movie': movie})