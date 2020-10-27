from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'awwards/project/(\d+)',views.rate_project,name='rate-project'),
    url(r'awwards/profile/(\d+)',views.view_profile,name='view-profile'),
    url(r'^search/', views.search_project, name='search_project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
