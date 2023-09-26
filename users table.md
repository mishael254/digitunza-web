*****************************
users table
userID
username
lastNamefirstName
email
phone
userCategory
status [active/t/f]

*****************************
user category tables
userCategoryId
userCategoryName

*****************************
partners table
parnerId 
userID [FK_USER]
organizationName
*****************************
project category tables
projectCategoryId
projectcategoryName

*****************************
project Sub category tables
projectSubCategoryId
projectCategoryId[FK]
projectSubcategoryName
*****************************
Country table
countryId
countryName

*****************************
county tables
countryId[fk]
countyName

*****************************

project table
projectId 
projectCategoryId[fk]
partnerId[fk]
projectName
projectCountryid[fk]
projectCountyId[fk]
projectZone
projectStartDate
projectEndDate
projectGroupNo ,int
projectAnthem ,audio
projectTheme ,img

*****************************
project officer tables
userId[fk]
projectOfficerName
projectOfficerEmail
projectofficerPassword
projectCategory
userCategory

*****************************
language table
languageId
languageName

*****************************
groups table
groupId
groupName
groupLeader[fk] ,blank = true, null=true
projectId[fk]
languageId[fk]

*****************************
Members table
membersId
groupId[fk]
membersFirstName
membersLastName
membersEmail
membersPhone
memberGender
memberAge
memberOccupation
memberCategory , blank=true , null=true

*****************************
group leaders table
groupleadersId
memberId[fk]
groupLeadersFname
groupleadersLname
groupLeadersemail
groupLeadersPhone
projectCategory
groupId[fk]

*****************************
Message table
messageId
messageTitle
messageTopic
messageSubTopic
messageDescription
messageLength
messageType [video,audio]
projectId[fk]
languageId[fk]
projectCategory[fk]
projectSubcategory[fk] ->subset of major categories

*****************************
SQL LITE IN MOBILE

*****************************
Members table
membersId
groupId ,blank = true, null = true
membersFirstName
membersLastName
membersEmail
membersPhone
memberGender
memberAge
memberOccupation
memberCategory , blank=true , null=true


*****************************
Usage Logs table
messagelogid
messageId[fk]
memberId [fk]
startTime
endTime

*****************************

Messages  table [L]
messageId
messageTitle
messageTopic
messageSubTopic
messageDescription
messageLength
messageCompleted , [true/false]









