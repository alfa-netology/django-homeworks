"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from datetime import datetime

from django.contrib import admin
from django.urls import path, register_converter

import books.views


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    # format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


register_converter(DateConverter, 'date')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books.views.index),
    path('books/', books.views.catalog, name='catalog'),
    path('books/<date:date>', books.views.page, name='page')
]
