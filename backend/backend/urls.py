"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import RegionViewSet, CommuneViewSet, QuartierViewSet, \
    DepartementViewSet, GenerateDBView
from api.pdf import ViewPDF, DownloadPDF

router = routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'departements', DepartementViewSet)
router.register(r'communes', CommuneViewSet)
router.register(r'quartiers', QuartierViewSet)
urlpatterns = [
    url(r'^generate_db/$', GenerateDBView.as_view()),
    url(r'^pdf_view/$', ViewPDF.as_view()),
    url(r'^pdf_download/$', DownloadPDF.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
