from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
class PartnerAdmin(ImportExportModelAdmin):
    list_display = ('organizationName',)
    list_display_links=('organizationName',)

admin.site.register(Partner, PartnerAdmin)

class ProjectCategoryAdmin(ImportExportModelAdmin):
    list_display = ('projectcategoryName',)
    list_display_links=('projectcategoryName',)

admin.site.register(ProjectCategory, ProjectCategoryAdmin)

class ProjectSubCategoryAdmin(ImportExportModelAdmin):
    list_display = ('projectCategoryId','projectSubcategoryName',)
    list_display_links=('projectCategoryId',)

admin.site.register(ProjectSubCategory, ProjectSubCategoryAdmin)

class CountyAdmin(ImportExportModelAdmin):
    list_display = ('countyName',)
    list_display_links=('countyName',)

admin.site.register(County, CountyAdmin)

class CountryAdmin(ImportExportModelAdmin):
    list_display = ('countryName',)
    list_display_links=('countryName',)

admin.site.register(Country, CountryAdmin)

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('projectName','partner','projectCategory','projectCountry','projectCounty','projectZone','projectGroupNo','projectStartDate','projectEndDate')
    list_display_links=('projectName',)

admin.site.register(Project, ProjectAdmin)

class ProjectOfficerAdmin(ImportExportModelAdmin):
    list_display = ('user','project')
    list_display_links=('user',)

admin.site.register(ProjectOfficer, ProjectOfficerAdmin)


class LanguageAdmin(ImportExportModelAdmin):
    list_display = ('languageName',)
    list_display_links=('languageName',)

admin.site.register(Language, LanguageAdmin)

class GroupAdmin(ImportExportModelAdmin):
    list_display = ('groupName','projectId','languageId')
    list_display_links=('groupName',)

admin.site.register(Group, GroupAdmin)

class MemberAdmin(ImportExportModelAdmin):
    list_display = ('groupId','membersFirstName','membersLastName','membersEmail','membersPhone','memberGender','memberAge','memberOccupation','memberCategory')
    list_display_links=('groupId',)

admin.site.register(Member, MemberAdmin)

class GroupLeaderAdmin(ImportExportModelAdmin):
    list_display = ('memberId','groupId','latitude','longitude')
    list_display_links=('memberId',)

admin.site.register(GroupLeader, GroupLeaderAdmin)

