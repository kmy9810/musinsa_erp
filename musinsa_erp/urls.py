from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('erp/', views.erp, name='erp'),
    path('erp/<int:id>', views.inventory, name='inventory'),
    path('erp/list/<int:id>', views.show_list, name='show-list'),
    path('erp/delete/<int:id>', views.delete_erp, name='delete-erp'),
    path('erp/delete-inventory/<int:id>', views.delete_inventory, name='delete-inventory'),
]
