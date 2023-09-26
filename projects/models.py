from django.db import models
from accounts.models import User


class Partner(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    organizationName = models.CharField(max_length=255)

    def __str__(self):
        return str(self.organizationName)

class ProjectCategory(models.Model):
    projectcategoryName = models.CharField(max_length=80)
    
    def __str__(self):
        return str(self.projectcategoryName)

class ProjectSubCategory(models.Model):
    projectCategoryId = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    projectSubcategoryName = models.CharField(max_length=80)

    def __str__(self):
        return str(self.projectSubcategoryName)

class Country(models.Model):
    countryName = models.CharField(max_length=40,default="Kenya")

    def __str__(self):
        return str(self.countryName)

class County(models.Model):
    countyName = models.CharField(max_length=30)

    def __str__(self):
        return str(self.countyName)

class Project(models.Model):
    projectName = models.CharField(max_length=255)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    projectCategory = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    projectCountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    projectCounty = models.ForeignKey(County, on_delete=models.CASCADE)
    projectZone = models.CharField(max_length=255)
    projectStartDate = models.DateField()
    projectEndDate = models.DateField()
    projectGroupNo = models.IntegerField()

    #******WORK ON UPLOAD TO GOOGLE DRIVE ******
    projectAnthem = models.FileField(blank=True,null=True)
    projectTheme = models.FileField(blank=True,null=True)

    def __str__(self):
        return ("%s , %s "  (self.projectName,self.projectZone))

class ProjectOfficer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return ("%s , %s"  (self.project,self.user.first_name,self.user.last_name,))
    
class Language(models.Model):
    languageName = models.CharField(max_length=255)

    def __str__(self):
        return str(self.languageName)
class Group(models.Model):
    groupName = models.CharField(max_length=255)
    #groupLeader = models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True, null=True)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return ("%s , %s, %s "  (self.groupName,self.groupLeader,self.projectId))

class Member(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    membersFirstName = models.CharField(max_length=255)
    membersLastName = models.CharField(max_length=255)
    membersEmail = models.EmailField()
    membersPhone = models.CharField(max_length=20)
    memberGender = models.CharField(max_length=10)
    memberAge = models.IntegerField()
    memberOccupation = models.CharField(max_length=255)
    memberCategory = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return ("%s , %s "  (self.membersFirstName,self.membersLastName))




class GroupLeader(models.Model):
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return ("%s , %s "  (self.memberId,self.groupId))



