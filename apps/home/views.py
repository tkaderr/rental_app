from django.shortcuts import render

# Create your views here.(
def index(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'home/home_page.html', context)


def user_dashboard(request):
    return redirect('/user_dashboard')

def edit_profile(request):
    return redirect('/edit_profile')

def search(request):
    pass
