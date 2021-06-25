from django.contrib import admin
from django.urls import path, include


# If no API version is specified, we will return rendered HTML pages instead
# of JSON response
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'^$', index, name="index"),
]
