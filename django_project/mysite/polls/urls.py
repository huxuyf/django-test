from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('name/',views.get_name),
    path('thanks/',views.thanks,name='thanks'),
    path('question_input/',views.question_input,name='question_input')

]
