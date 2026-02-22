from rest_framework import serializers

class StudentPerformanceSerializers(serializers.Serializer):
    gender = serializers.CharField(max_length=32)
    race_ethnicity = serializers.CharField(max_length=50)
    parental_level_of_education =  serializers.CharField(max_length=50)
    lunch = serializers.CharField(max_length=32)
    test_preparation_course = serializers.CharField(max_length=50)
    reading_score = serializers.IntegerField()
    math_score = serializers.IntegerField()
