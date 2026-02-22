from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import StudentPerformanceSerializers
import joblib
import os
from django.conf import settings

scaler_path = os.path.join(settings.BASE_DIR, 'student_scaler.pkl')
scaler = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'student_model.pkl')
model = joblib.load(model_path)

gender = ['male']
race_ethnicity = ['group B', 'group C', 'group D' , 'group E']
parental_level_of_education = ["bachelor's degree", 'high school', "master's degree", 'some college', 'some high school']
lunch = ['standard']
test_preparation_course = ['none']

class StudentPredict(views.APIView):
 def post(self, request):
     serializer = StudentPerformanceSerializers(data=request.data)
     if serializer.is_valid():
         data = serializer.validated_data
         new_gender = data.get('gender')
         gender1or_0 = [1 if new_gender == i else 0 for i in gender]

         new_race = data.get('race_ethnicity')
         race1or_0 = [1 if new_race == i else 0 for i in race_ethnicity]

         new_parental = data.get('parental_level_of_education')
         parental1or_0 = [1 if new_parental == i else 0 for i in parental_level_of_education]

         new_lunch = data.get('lunch')
         lunch1or_0 = [1 if new_lunch == i else 0 for i in lunch]

         new_test = data.get('test_preparation_course')
         test1or_0 = [1 if new_test == i else 0 for i in test_preparation_course]

         features = [data['reading_score'], data['math_score']] + gender1or_0 + race1or_0 + parental1or_0 + lunch1or_0 + test1or_0
         scaled_data = scaler.transform([features])
         pred = model.predict(scaled_data)[0]
         # student = serializer.save(student_predicted=round(pred))

         return Response({'Predict': round(pred)}, status.HTTP_200_OK)
     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
