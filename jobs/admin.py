from django.contrib import admin
from .models import Jobs, Referencias

# Register your models here.

class JobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'categoria', 'profissional', 'arquivo_final', 'status']
    
admin.site.register(Jobs, JobsAdmin)
admin.site.register(Referencias)
