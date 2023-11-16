from django.db import models

from users.models import UserProfile


class WebSite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class SiteStatistics(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    site = models.ForeignKey(WebSite, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    clicks = models.IntegerField(default=0)
    data_sent = models.IntegerField(default=0)
    data_received = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.site_name} - {self.user.user.username}"