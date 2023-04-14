from django.db import models

# from django.conf import settings
from app.user_auth.models import User


# department model added to prevent possible typos when entering department name,
# can be replaced by a select field, though incase of a new department the source code has to be updated(in case of select field)
class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(
        User, related_name="opportunity", on_delete=models.CASCADE
    )
    posted_on = models.DateField()
    application_deadline = models.DateField()
    description = models.TextField(blank=True, max_length=255, null=True)
    job_description = models.URLField(blank=True, null=True, verbose_name="JD Link")

    class Meta:
        verbose_name_plural = "Opportunities"
        ordering = ("-posted_on",)  # order by date posted. recent jobs first

    def __str__(self) -> str:
        return f"{self.title}"


class OpportunityRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} registered for {self.Opportunity} Opportunity"
