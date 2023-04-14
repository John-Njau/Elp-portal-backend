from django.contrib import admin

from app.opportunities.models import Opportunity, Department, OpportunityRegister


class OpportunityAdmin(admin.ModelAdmin):
    model = Opportunity
    list_display = (
        "id",
        "title",
        "department",
        "posted_by",
        "description"
    )


class OpportunityRegisterAdmin(admin.ModelAdmin):
    model = OpportunityRegister
    list_display = (
        "id",
        "user",
        "Opportunity"
    )

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = (
        "id",
        "name"
    )


# register models to admin interface
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(OpportunityRegister, OpportunityRegisterAdmin)
