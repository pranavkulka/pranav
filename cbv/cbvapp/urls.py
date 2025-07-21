from django.urls import path
from cbvapp import views

urlpatterns =[
    path('',views.Allcompanies.as_view(), name='list'),
    path('<int:pk>/',views.CompanyDetails.as_view(), name='detail'),
    path('create/',views.Allcompany.as_view(), name='create'),
    path('update/<int:pk>/',views.CompanyUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.CompanyDelete.as_view(), name='delete'),
    path('', views.myclass.as_view(), name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/', views.logout_view, name='logout')
]