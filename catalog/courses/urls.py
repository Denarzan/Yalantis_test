from django.urls import path
from .views import CoursesDetailView, CoursesListView

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses'),
    path('<int:id>/', CoursesDetailView.as_view(), name='detail'),
]