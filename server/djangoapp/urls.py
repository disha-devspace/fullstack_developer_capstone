from django.urls import path
from . import views

urlpatterns = [
    path('dealers/', views.get_all_dealers),
    path('dealer/<int:dealer_id>/', views.get_dealer_by_id),
    path('dealers/state/<str:state>/', views.get_dealers_by_state),
    path('dealer/<int:dealer_id>/reviews/', views.get_dealer_reviews),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
