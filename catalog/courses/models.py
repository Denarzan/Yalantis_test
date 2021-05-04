from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positive(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is not an positive number. Lectures must be more than 1.'),
            params={'value': value},
        )


class Course(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    num_of_lectures = models.SmallIntegerField(verbose_name="Number of lectures", validators=[validate_positive])
