from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('erp/', views.erp, name='erp'),
    path('erp/<int:id>', views.inventory, name='inventory'),
    path('erp/delete/<int:id>', views.delete_erp, name='delete-erp'),
]
