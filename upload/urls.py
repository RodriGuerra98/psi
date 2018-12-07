from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from upload import views


urlpatterns = [
    url(r'^upload/add_workflow/$', views.add_workflow, name="add_workflow"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
