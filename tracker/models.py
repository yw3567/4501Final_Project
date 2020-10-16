from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Longitude = models.FloatField(
    help_text = _('x'),
    )

    Latitude = models.FloatField(
    help_text = _('y'),
    )

    Unique_Squirrel_ID = models.CharField(
    max_length = 100,
    help_text = _('Unique Squirrel ID'),
    )        

    #Hectare = models.CharField(
    #max_length = 50,
    #help_text = _('Hectare'),
    #)

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
    (AM, _('AM')),
    (PM, _('PM')),
    ]

    Shift = models.CharField(
    max_length = 25,
    choices = SHIFT_CHOICES,
    help_text = _('Shift'),
    )

    Date = models.DateField(
    help_text = _('Date'),
    blank = True,
    )

    #Hectare_Squirrel_ID = models.IntegerField(
    #help_text = _('Hectare Squirrel ID'),
    #blank = True,
    #)        
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICES = [
    (Adult, _('Adult')),
    (Juvenile, _('Juvenile')),
    ]

    Age = models.CharField(
    max_length = 25,
    choices = AGE_CHOICES,
    help_text = _('Choices of Age'),
    blank = True,
    null = True,
    )

    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'

    FUR_COLOR_CHOICES = [
    (Gray, _('Gray')),
    (Cinnamon, _('Cinnamon')),
    (Black, _('Black')),
    ]

    Primary_Fur_Color = models.CharField(
    max_length = 25,
    choices = FUR_COLOR_CHOICES,
    help_text = _('Choices of Fur Color'),
    blank = True,
    null = True,
    )

    #Highlight_Fur_Color = 

    #Combination_of_Primary_and_Highlight_Color = 

    #Color notes = 
    

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'

    LOCATION_CHOICES = [
    (Ground_Plane, _('Ground Plane')),
    (Above_Ground, _('Above_Ground')),
    ]
    
    Location = models.CharField(
    max_length = 25,
    choices = LOCATION_CHOICES,
    help_text = _('Choices of Location'),
    blank = True,
    null = True,
    )

    #Above_Ground_Sighter_Measurement = 

    Specific_Location = models.CharField(
    max_length = 25,
    help_text = _('Specific Location'),
    blank = True,
    null = True,
    )

    TRUE = 'True'
    FALSE = 'False'

    CHOICES = [
    (TRUE, _('True')),
    (FALSE, _('False')),
    ]

    Running = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Choices of Running'),
    blank = True,
    null = True,
    )

    Chasing = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Choices of Chasing'),
    blank = True,
    null = True,
    )

    Climbing = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Choices of Climbing'),
    blank = True,
    null = True,
    )

    Eating = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Choices of Eating'),
    blank = True,
    null = True,
    )

    Foraging = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Choices of Foraging'),
    blank = True,
    null = True,
    )

    Other_Activities = models.CharField(
    max_length = 50,
    help_text = _('Other Activities'),
    blank = True,
    null = True,
    )

    Kuks = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Kuks'),
    blank = True,
    null = True,
    )

    Quaas = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Quaas'),
    blank = True,
    null = True,
    )

    Moans = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Moans'),
    blank = True,
    null = True,
    )

    Tail_flags = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Tail Flags'),
    blank = True,
    null = True,
    )

    Tail_twitches = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Tail Twitches'),
    blank = True,
    null = True,
    )

    Approaches = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Approaches'),
    blank = True,
    null = True,
    )

    Indifferent = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Indifferent'),
    blank = True,
    null = True,
    )

    Runs_from = models.CharField(
    max_length = 25,
    choices = CHOICES,
    help_text = _('Runs From'),
    blank = True,
    null = True,
    )

    #Other_interactions = 

    #Lat_Long = 



# Create your models here.
