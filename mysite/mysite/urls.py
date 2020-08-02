"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import include, url
from myapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', v.index),
    path('',v.index),
    path('classificacao_rodada.html', v.classificacao_rodada),
    path('classificacao_mes.html', v.classificacao_mes),
    path('classificacao_geral.html', v.classificacao_geral),
    path('prox_rodada.html', v.prox_rodada),
    path('regulamento.html', v.regulamento),
    path('rodada_depois.html', v.rodada_depois),
    path('rodada_seguinte.html', v.rodada_seguinte),
    path('galeria_campeoes.html', v.galeria_campeoes)
]

urlpatterns += staticfiles_urlpatterns()