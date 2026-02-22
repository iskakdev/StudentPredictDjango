from tkinter.font import names

from django.urls import path
from .views import StudentPredict

urlpatterns = [
    path('predict/', StudentPredict.as_view(), name='student_predict')
]