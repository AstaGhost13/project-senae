"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from core_apps.common.views import IndexView

#urls de la aplicacion
urlpatterns = [
    path('admin/', admin.site.urls),

     # Aplicaciones locales
    #path('common/', include('core_apps.common.urls')),
    path('', IndexView.as_view(), name='index'),  # Ruta para la página de inicio
    path('account/', include('core_apps.account.urls')),
    path('computing-infrastructure/', include('core_apps.computing_infrastructure.urls')),
    path('organizational-structure/', include('core_apps.organizational_structure.urls')),
    path('stock-management/', include('core_apps.stock_management.urls')),

]
