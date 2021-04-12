from  django.urls import path
from .views import index, detail, result, vote
urlpatterns = [
    path('', index, name="index"),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results', result, name='result'),
    path('<int:question_id>/vote', vote, name='vote'),
]