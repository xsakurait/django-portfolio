from django.contrib import admin

from .models import Description,Skill,Profile,Works

# Register your models here.
admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Skill)
admin.site.register(Works)

