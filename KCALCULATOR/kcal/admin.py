from django.contrib import admin
from .models import Food
# Register your models here.
@admin.action(description='Mark selected food as accepted')
def make_accepted(modeladmin, request, queryset):
    queryset.update(status='confirmed')
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "status"]
    actions = [make_accepted]
    pass

