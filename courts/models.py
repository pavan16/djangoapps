from django.db import models


COURT_TYPE= (
    ('wooden', 'wooden'),
    ('polymer', 'polymer'),
)


SHOES_TYPE_ALLOWED= (
    ('Marking shoes', 'Marking shoes'),
    ('Non Marking shoes', 'Non Marking shoes'),
    ('Both', 'Both'),
)


OPEN_COURT_TYPE= (
    ('Open to air', 'Open to air'),
    ('Closed', 'Closed'),
)


class Court(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    locality = models.CharField(max_length=200, default='SOME STRING')
    city = models.CharField(max_length=200)
    court_type= models.CharField(max_length=10, choices=COURT_TYPE)
    shoes_type_allowed = models.CharField(max_length=10, choices=SHOES_TYPE_ALLOWED)
    open_court_type = models.CharField(max_length=10, choices=OPEN_COURT_TYPE)
