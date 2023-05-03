from django.contrib import admin

from .models import User,Project,Revision,Data,DataExtra,Dimension,DimensionCalc,Stack,StackLine,UploadImageTest
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Revision)
admin.site.register(Data)
admin.site.register(DataExtra)
admin.site.register(Dimension)
admin.site.register(DimensionCalc)
admin.site.register(Stack)
admin.site.register(StackLine)
admin.site.register(UploadImageTest)