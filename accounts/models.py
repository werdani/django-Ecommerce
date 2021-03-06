from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls.base import reverse
import datetime
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify
#for signals.
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user =models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    image =models.ImageField(_("image"),upload_to='profile_img',blank=True, null=True)
    countrey = CountryField()
    address =models.CharField(_("address"), max_length=100)
    join_date =models.DateTimeField(_("join date"), default =datetime.datetime.now)
    slug =models.SlugField(_("slug"),blank=True, null=True)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user)

    def get_absolute_url(self):
        return reverse("accountes:Profile_detail", kwargs={"slug": self.slug})

#def for signals.
def add_profile(sender,**kwargs):
 #if create user signals send 'created' for add_profile.
    if kwargs['created']:
        user_profile =Profile.objects.create(user=kwargs['instance'])

#to connect this function and signals use post_save.
post_save.connect(add_profile,sender=User)
