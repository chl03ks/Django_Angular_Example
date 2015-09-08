from django.db import models
from django.db.models import permalink


class Instructional(models.Model):
    title = models.CharField(max_length=512, unique=True)
    body = models.TextField()
    source = models.CharField(max_length=512)

    def __unicode__(self):
        return u"{title}".format(title=self.title)

    @permalink
    def get_absolute_url(self):
        return('view_instructional', None, {'pk': self.pk})


class Question(models.Model):
    instructional = models.ForeignKey(Instructional, related_name='questions')
    question_content = models.TextField()
    answer = models.BooleanField(help_text="""If it is unchecked the answer is False if it is checked the answer is True.""")

    def __unicode__(self):
        return u"{instructional}".format(instructional=self.instructional)
