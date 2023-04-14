from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'register', views.ChapterRegisterViewSet, basename='chapter_register')
router.register(r'', views.ChapterViewSet)

urlpatterns = [
    path('chapters/', include(router.urls)),
    path('chapters/search/<str:chapter_name>', views.SearchChapter.as_view()),
]
