# from tkinter import Image
from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.template.loader import get_template

from .models import (
    Supplier,
    Yard,
    # metal, 
    cost, grade
)
from .forms import(
    YardForm
)
# class demoAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in demo._meta.get_fields()]

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class YardAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

# class metalAdmin(admin.ModelAdmin):
#     list_display = ['name', 'rate']

class gradeAdmin(admin.ModelAdmin):
    # inlines = (ImageAdminInline,)
    list_display = [field.name for field in grade._meta.get_fields()] 

    # def image_inline(self, obj=None, *args, **kwargs):
    #     context = obj.response['context_data']
    #     inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
    #     return get_template(inline.opts.template).render(context, obj.request)

    # def render_change_form(self, request, context, *args, **kwargs):
    #     instance = context['adminform'].form.instance  # get the model instance from modelform
    #     instance.request = request
    #     instance.response = super().render_change_form(request, context, *args, **kwargs)
    #     return instance.response   



admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Yard, YardAdmin)
# admin.site.register(metal, metalAdmin)
admin.site.register(grade, gradeAdmin)
# admin.site.register(demo, demoAdmin)
# admin.site.register(cost_grade,ImageAdminInline)
# admin.site.register(Yard, YardAdmin)
