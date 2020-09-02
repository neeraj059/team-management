# System and Django libraries

from django.utils import timezone
from django.db import models

from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser

from team.constants import ROLES


class TeamMembers(AbstractBaseUser):
    """
    Model to store team member details
    """

    first_name = models.CharField(_('First Name'), max_length=60, null=False)

    last_name = models.CharField(_('Last Name'), max_length=60, blank=False, null=False)

    phone_number = PhoneNumberField(_('Phone number'), blank=False, null=False,
                                    help_text='Phone number with country code',
                                    unique=True,
                                    db_index=True
                                    )

    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
        db_index=True
    )

    role = models.CharField(_('Role'), max_length=20, choices=ROLES,
                            blank=False, null=False)

    is_active = models.BooleanField(_('Is User Active'), default=True)

    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
