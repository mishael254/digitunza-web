from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
class MessageAdmin(ImportExportModelAdmin):
    list_display = ('messageTitle','messageTopic','messageSubTopic','messageDescription','messageLength','messageType','projectId','languageId','projectCategory','projectSubcategory','messagefile','dateuploaded')
    list_display_links=('messageTitle',)

admin.site.register(Message, MessageAdmin)

class UsageLogAdmin(ImportExportModelAdmin):
    list_display = ('messageId','memberId','startTime','endTime','messageLength','messageCompleted','dateloged')
    list_display_links=('messageId',)

admin.site.register(UsageLog, UsageLogAdmin)
