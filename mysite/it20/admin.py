from django.contrib import admin
from it20.models import newIdea
from import_export.admin import ImportExportModelAdmin

#admin.site.register(idea)
#admin.site.register(newIdea)
@admin.register(newIdea)

class newIdea(ImportExportModelAdmin):
    pass
