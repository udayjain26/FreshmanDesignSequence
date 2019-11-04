"""findapartner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from users.views import home
from events.views import events, event_page
from events.views import newEvents
from django.urls import include, path
from users.views import faqpage
from users.views import contactpage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("", home, name ="home"),
    path('users/', include('django.contrib.auth.urls')),
    path("events/", events, name ="events"),
    path("event/", event_page, name ="event"),
    path("events/new/", newEvents, name = "newEvents"),
    path('users/', include('users.urls')),
    path('faq/', faqpage, name = 'faqpage'),
    path('contact/', contactpage, name = 'contactpage')
]
