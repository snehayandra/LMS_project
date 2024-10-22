from django.urls import path
from.import views
urlpatterns=[
    path('',views.dpprocessing),
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view()),
    path('student/',views.StudentList.as_view()),
     path('student/<int:pk>/',views.TeacherDetail.as_view()),
    
    
]
