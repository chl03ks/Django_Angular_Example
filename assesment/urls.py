from django.conf.urls import url, include, patterns

from rest_framework import routers

from .views import InstructionalViewSet
from .views import QuestionViewSet
from .views import QuestionDetail
from assesment import views

router = routers.DefaultRouter()
router.register(r'instructional', InstructionalViewSet)
router.register(r'questions', QuestionViewSet)

questions_urls = patterns('', url(r'^(?P<pk>\d+)$', QuestionDetail.as_view(), name='questions-detail'))


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^(?P<pk>\d+)/$', 'assesment.views.view_instructional', name='view_instructional'),
    url(r'^api/questions/', include(questions_urls)),
]
