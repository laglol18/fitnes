from django.urls import path

from activator_app import views
app_name = 'demo'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('', views.index, name='home'),
    path('about-us.html/', views.about_us, name='about-us'),
    path('blog-single.html/', views.blog_single, name='blog-single'),
    path('blog.html/', views.blog, name='blog'),
    path('contact.html/', views.contact, name='contact'),
    path('gallery.html/', views.gallery, name='gallery'),
    path('schedule.html/', views.schedule, name='schedule'),
    path('main/', views.main, name='main_page')
]