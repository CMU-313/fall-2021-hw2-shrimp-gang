
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


## https://docs.djangoproject.com/en/3.2/topics/db/models/
'''
 Creates a class for the candidates/reviewees and stores their GPA, Undergraduate
 college, and Undergraduate major.
'''
class Candidate(models.Model):
    gpa = models.DecimalField(
    max_digits=3, decimal_places=2, help_text=_('GPA of the candidate'))

    undergrad_uni = models.CharField(
    max_length=255, help_text=_('Undergraduate University of the candidate.'),
    verbose_name=_('undergrad_uni'))

    major = models.CharField(
    max_length=255, help_text=_('Undergraduate Major of the candidate.'),
    verbose_name=_('major'))

'''
Creates a class for the reviewers and stores their name and all the ratings they assign
the reviewers.
'''
class Reviewer(models.Model):
    name = models.CharField(
    max_length=255, help_text=_('Name of the reviewer.'),
    verbose_name=_('Name'))
    
    total_rating = models.PositiveSmallIntegerField(
    help_text=_('Overall Rating of candidate.'),
    verbose_name=_('Overall Rating'))

    letters_of_rec = models.PositiveSmallIntegerField(
    help_text=_('Rating of Letters of Recommendation of candidate.'),
    verbose_name=_('Letters of Recommendation Rating'))

    interview = models.PositiveSmallIntegerField(
    help_text=_('Interview Rating of candidate.'),
    verbose_name=_('Interview Rating'))

    essay = models.PositiveSmallIntegerField(
    help_text=_('Essay Rating of candidate.'),
    verbose_name=_('Essay Rating'))

    extracurriculars = models.PositiveSmallIntegerField(
    help_text=_('Extracurriculars Rating of candidate.'),
    verbose_name=_('Extracurriculars Rating'))

    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
