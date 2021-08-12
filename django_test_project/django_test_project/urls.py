from django.contrib import admin
from django.urls import path, include
from crawler_app.views import index
from rest_framework import routers
import crawler_app.views

router = routers.DefaultRouter()
router.register("deals", crawler_app.views.DealViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("api/", include(router.urls)),
]
