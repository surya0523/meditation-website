# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('therapy/', views.therapy_page, name='therapy'),
#     path('family-therapy/', views.family_therapy_page, name='family_therapy'),
#     path('therapy/<int:service_id>/', views.service_detail, name='service_detail'),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('therapy/', views.therapy_page, name='therapy'),
#     path('therapy/<int:service_id>/', views.service_detail, name='service_detail'),
#     path('therapy/family-therapy/', views.family_therapy, name='family_therapy'),
# ]

from django.urls import path
from . import views 
from .views import login_view, register_view

urlpatterns = [
    path('', views.home, name='home'),
    path('therapy/', views.therapy_page, name='therapy'),
    path('therapy/family-therapy/', views.family_therapy, name='family_therapy'),
    # இந்த புதிய URL-களைச் சேர்க்கவும்
    path('therapy/individual-therapy/', views.individual_therapy, name='individual_therapy'),
    path('therapy/couples-therapy/', views.couples_therapy, name='couples_therapy'),
    path('therapy/online-therapy/', views.online_therapy, name='online_therapy'),
    path('therapy/group-therapy/', views.group_therapy, name='group_therapy'),
    path('submit_form/', views.submit_approach_form, name='Approach_form'),
    path('approach_form/', views.approach_form_view, name='approach_form'),
    path('payment/', views.payment_view, name='payment'),
    path('about/', views.about_view, name='about'),
    path('meditation/', views.meditation_view, name='meditation'),
    path('discover-popular-meditations/', views.discover_meditations_view, name='discover_popular_meditations'),
    path('contact/', views.contact_view, name='contact'),
    path('search/', views.search_results, name='search_results'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
