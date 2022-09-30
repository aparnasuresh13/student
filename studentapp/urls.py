from studentapp import views
from django.urls import path

urlpatterns=[

 path('',views.add_student,name='add_student'),
 path('add_student_details',views.add_student_details,name='add_student_details'),
 path('show_details',views.show_details,name='show_details'),

 path('editpage/<int:pk>',views.editpage,name='editpage'),
 path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
 path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
 path('delete_student/<int:pk>',views.delete_student,name='delete_student')
]