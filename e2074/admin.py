from django.contrib import admin

# Register your models here.
from .models import Party,Candidate,Post,Feedback,Zone,District,Vdc,Municipality

class CandidateAdmin(admin.ModelAdmin):
    list_display=("id","name", "party","criminalcase")
    prepopulated_fields = {"slug":("name",)}

class PartyAdmin(admin.ModelAdmin):
    list_display=("id","name")
    prepopulated_fields = {"slug":("name",)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = {'slug':('title',)}

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','whatyouweredoing','whathappened']

class ZoneAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','name','zone']

class VdcAdmin(admin.ModelAdmin):
    list_display = ['id','name','zone', 'district']

class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ['id','name','zone', 'district']


admin.site.register(Party, PartyAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Vdc, VdcAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
