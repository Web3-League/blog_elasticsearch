from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from .models import Robot

@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('robot_actions',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Si vous voulez rediriger par défaut vers la liste des robots
        return HttpResponseRedirect(reverse('api:api:robot:robot_list'))

    def robot_actions(self, obj):
        # Boutons d'action personnalisés (exemple)
        return format_html('<a class="button" href="{}">List Robots</a>&nbsp;',
                           reverse('api:api:robot:robot_list')
                           )
 

    robot_actions.short_description = 'Robot Actions'
    robot_actions.allow_tags = True

# Register your models here.
#
    






