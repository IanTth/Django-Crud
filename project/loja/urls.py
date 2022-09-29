from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'cadastro_produto', views.cadastro_produto),
    url(r'consulta_produto', views.consulta_produto),
    url(r'', views.home),
    

] + static(settings.STATIC_URL)
