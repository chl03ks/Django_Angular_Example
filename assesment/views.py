from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404

from rest_framework import viewsets, permissions, generics

from .serializers import InstructionalSerializer, QuestionSerializer
from .models import Instructional, Question


class InstructionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows instructional
    content to be views or edited
    """
    queryset = Instructional.objects.all()
    serializer_class = InstructionalSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Question
    content to be views or edited
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Question
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Question.objects.all()


def index(request):
    return render(request, 'assesments/index.html')


def view_instructional(request, pk):
    instructional = get_object_or_404(Instructional, id=pk)
    return render_to_response('assesments/view_instructional.html',
                               {'instructional': instructional})
