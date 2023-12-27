from django.shortcuts import render
from Product.models import catagory

# Create your views here.
def Home(request):
    all_cata = catagory.objects.all()
    return render(request, 'Home/home.html', locals())
