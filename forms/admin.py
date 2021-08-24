from django.contrib import admin

from .models import *

from django.contrib.admin.options import ModelAdmin

admin.site.site_header = 'Donkey Survey Administration'                     # default: "Django Administration"
admin.site.index_title = 'Donkey Survey Database Structure'                 # default: "Site administration"
admin.site.site_title = 'Donkey Survey Site Admin'                          # default: "Django site admin"



admin.site.register(Form)
admin.site.register(Response)
admin.site.register(Question)