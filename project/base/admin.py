from django.contrib import admin
from .models import Courses_model, DT_model, Desires_model, Days_model, User

# Register your models here.

admin.site.register(Courses_model)
admin.site.register(DT_model)
admin.site.register(Desires_model)
admin.site.register(Days_model)
admin.site.register(User)



