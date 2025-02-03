from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('waste_app.urls')),  # Include URLs from waste_app
    # path('accounts/', include('django.contrib.auth.urls')),  # Built-in authentication URLs
]
