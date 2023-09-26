from django.db import models

from projects.models import Project,Language,ProjectCategory,ProjectSubCategory,Member

class Message(models.Model):
    messageTitle = models.CharField(max_length=255)
    messageTopic = models.CharField(max_length=255)
    messageSubTopic = models.CharField(max_length=255)
    messageDescription = models.TextField()
    messageLength = models.IntegerField()
    messageType = models.CharField(max_length=10, choices=[('video', 'Video'), ('audio', 'Audio')])
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    projectCategory = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    projectSubcategory = models.ForeignKey(ProjectSubCategory, on_delete=models.CASCADE, null=True)
        #******WORK ON UPLOAD TO GOOGLE DRIVE ******
    messagefile = models.FileField()
    dateuploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s , %s , %s" % (self.messageTitle,self.messageTopic,self.dateuploaded))
    

class UsageLog(models.Model):
    messageId = models.ForeignKey(Message, on_delete=models.CASCADE)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    messageLength = models.IntegerField()
    messageCompleted = models.BooleanField(default=False) 
    dateloged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s , %s , %s" % (self.messageId,self.memberId ,self.dateloged))