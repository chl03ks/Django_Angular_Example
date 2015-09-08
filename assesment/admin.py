from django.contrib import admin

from .models import Instructional
from .models import Question


admin.site.register(Instructional)
admin.site.register(Question)
