from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from find import views


urlpatterns = [
    url(r'^$', views.workflow_list, name='list'),
    url(r'^workflow_list/(?P<category_slug>[-\w]+)/$', views.workflow_list, name='list'),
    url(r'^workflow_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_detail, name='workflow_detail'),
    url(r'^workflow_search/$', views.workflow_search, name='workflow_search') ,
    url(r'^workflow_download/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_download, name="workflow_download"),
    url(r'^workflow_download_json/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_download_json, name="workflow_download_json"),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
