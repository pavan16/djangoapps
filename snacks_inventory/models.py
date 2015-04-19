from django.db import models


class User(models.Model):

    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()


class Snack(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    original_quantity = models.IntegerField(default=0)
    remaining_quantity = models.IntegerField(default=0, null=True)
    date_consumed = models.DateTimeField('date consumed', null=True)


class SnackConsumer(models.Model):

    def __str__(self):
        return self.consumed_snack_name.name

    consumed_snack_name = models.ForeignKey(Snack)
    consumed_user = models.ForeignKey(User)
    consumed_quantity = models.IntegerField(default=0)
    date_consumed = models.DateTimeField('date consumed', null=True)