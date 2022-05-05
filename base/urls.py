from django.urls import path, reverse_lazy, include

from django.contrib.auth import views as auth_views

from base.views import Home, EmpresaView



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('empresa/', EmpresaView.as_view(), name='empresa_list'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), 
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
     next_page=reverse_lazy('base:login')), name='logout'),    

]
