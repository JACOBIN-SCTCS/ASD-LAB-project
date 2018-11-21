from django.urls import path
from . import views
from .views import TodoUpdateView

app_name="main"

urlpatterns=[
    
            path('',views.index,name='index'),
            path('add/',views.addtodopage,name='addtodo'),
            path('update/<int:pk>',TodoUpdateView.as_view(),name='update'),
            path('delete/<int:id>',views.deletetodo,name='delete')
]   