from django.urls import path
from . import views



urlpatterns = [
    # ex: /student/
    path('', views.index, name='index'),

    # ex: /student/login
    path('login', views.login, name='login'),

     # ex: /student/office
    path('office', views.office, name='office'),

    # ex: /student/5/office/5/
    path('<int:student_id>/office/<str:office_id>/', views.detail, name='detail'),

    # ex: /student/office/5/transaction
    path('<int:student_id>/office/<str:office_id>/transaction/<str:transaction_id>', views.transaction, name='transaction'),

     # ex: /student/office/5/transaction/send_sms
    path('office/<int:question_id>/transaction/send_sms', views.send_sms, name='send_sms'),

]
