from django.shortcuts import render, redirect
from activator_app.forms import CreateUserForm


def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'about-us.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def blog_single(request):
    return render(request, 'blog-single.html')
def main(request):
    return render(request, 'main.html')
def schedule(request):
    return render(request, 'schedule.html')
def gallery(request):
    return render(request, 'gallery.html')


def registerPage(request):


    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'app/register.html', context)

