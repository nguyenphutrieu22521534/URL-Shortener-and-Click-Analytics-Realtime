from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ShortUrl(models.Model):
    longUrl = models.URLField(_("Website URL"), max_length=200)
    shortUrl = models.CharField(_("Short URL"), max_length=15)
    created = models.DateTimeField(_("Created Time"), auto_now=True)

    class Meta:
        verbose_name = _("ShortUrl")
        verbose_name_plural = _("ShortUrls")

    def __str__(self):
        return str(self.longUrl)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
