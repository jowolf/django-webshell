from django.contrib import admin
from .forms import ScriptForm
from .models import Script


class ScriptAdmin(admin.ModelAdmin):
    form = ScriptForm
    change_form_template = 'webshell/change_form.html'
    list_display = ['name', 'created', 'modified']
    date_hierarchy = 'created'
    save_on_top = True
    save_as = True

admin.site.register(Script, ScriptAdmin)