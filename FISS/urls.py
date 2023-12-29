from django.urls import path
from . import views


urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('income-revenue/', views.income_revenue_view, name='income_revenue'),
    path('expenses/', views.expenses_view, name='expenses'),
    path('analysis/', views.analysis_view, name='analysis'),
    path('education-library/', views.education_library_view, name='education_library'),
    path('', views.home_view, name='root'),
    path('registration/', views.registration_view, name='registration' ),
    path('finance-resource/', views.finance_resources_view, name='finance_resource'),
]
    

