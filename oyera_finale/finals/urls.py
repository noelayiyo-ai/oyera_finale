from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    # for the parts
    path('addpart/', views.addPart, name='addPart'),
    path('editpart/<int:part_id>', views.editPart, name='editPart'),
    path('viewpart/', views.partView, name='viewPart'),
    path('deletepart/', views.deletePart, name='deletePart')
]

