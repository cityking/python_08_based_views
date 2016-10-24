"""based_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from based_app.views import AddModelView, MyView, HomePageView, PoemCounterRedirectView, PoemDetailView, PoemListView 
from django.views.generic.base import RedirectView
from based_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myview/$', MyView.as_view(), name='my-view'),
 #   url(r'^home/$', HomePageView.as_view(), name='home'),
    url(r'^goto-baidu/$', RedirectView.as_view(url='http://www.baidu.com'), name='gotobaidu'),
    url(r'^$', views.home, name='home'),
    url(r'^counter/(?P<pk>\d+)/$', PoemCounterRedirectView.as_view(), name='counter' ),
    url(r'^details/(?P<pk>\d+)/$', PoemDetailView.as_view(), name='details'),
    url(r'^list/$', PoemListView.as_view(), name='list'),
    url(r'^add/$', AddModelView.as_view())

]

