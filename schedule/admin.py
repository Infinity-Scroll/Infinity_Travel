from django.contrib import admin
from .models import Planner, PeriodEvent, DateEvent

class DateEventInline(admin.TabularInline):
    model = DateEvent
    extra = 1

class PeriodEventInline(admin.TabularInline):
    model = PeriodEvent
    inlines = [DateEventInline]
    extra = 1

class PlannerAdmin(admin.ModelAdmin):
    inlines = [PeriodEventInline]

admin.site.register(Planner, PlannerAdmin)
admin.site.register(PeriodEvent)
admin.site.register(DateEvent)