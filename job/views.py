from django.shortcuts import render
from blog.models import blog
# Create your views here.
def home(request):
 blogs = blog.objects
 return render(request,'home.html',{'blog':blogs})