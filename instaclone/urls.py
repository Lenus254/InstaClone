from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('accounts/profile/',views.profile,name = 'profile'),
    path('search/profile', views.search, name='profileresults'),
    path('timeline', views.timeline, name='timeline'),
    path('edit_profile', views.edit_profile, name='edit'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)