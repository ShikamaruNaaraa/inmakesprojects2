from django.contrib import admin
from .models import Place,Actor
# Register your models here.
# def site():
#     return None

admin.site.register(Place)
admin.site.register(Actor)