from django.contrib import admin
from .models import Planners, PeriodEvents, DateEvents

class DateEventInline(admin.TabularInline):
    model = DateEvents
    extra = 1

class PeriodEventInline(admin.TabularInline):
    model = PeriodEvents
    inlines = [DateEventInline]
    extra = 1

class PlannerAdmin(admin.ModelAdmin):
    inlines = [PeriodEventInline]

admin.site.register(Planners, PlannerAdmin)
admin.site.register(PeriodEvents)
admin.site.register(DateEvents)