from django.contrib import admin
from stats.models import Point, Point_zn, Zn_limit, Point_limit
# Register your models here.

class PointAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

class Point_znAdmin(admin.ModelAdmin):
    list_display=('point','date', 'time', 'zn')

class Zn_limitAdmin(admin.ModelAdmin):
    list_display=('start_morning', 'end_morning', 'start_evening', 'end_evening')

class Point_limitAdmin(admin.ModelAdmin):
    list_display=('point', 'zn_morning', 'zn_evening')

admin.site.register(Point, PointAdmin)
admin.site.register(Point_zn, Point_znAdmin)
admin.site.register(Zn_limit, Zn_limitAdmin)
admin.site.register(Point_limit, Point_limitAdmin)
