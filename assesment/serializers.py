from rest_framework import serializers
from .models import Instructional, Question


class InstructionalSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='questions-detail'
    )

    class Meta:
        model = Instructional
        fields = ('id', 'title', 'body', 'source', 'questions')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'instructional', 'question_content', 'answer')
