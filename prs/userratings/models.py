from django.db import models

class Userprofile(models.Model):
	GENDER = (
		('m', 'Male'),
		('f', 'Female'),
	)
	COUNTRY = (
		('AF', 'Afghanistan'),
		('AX', 'Åland Islands'),
		('AL', 'Albania'),
		('DZ', 'Algeria'),
	)
	user = models.ForeignKey('auth.User')
	name = models.CharField(max_length=200)
	gender = models.CharField(choices=GENDER, max_length=1)
	country = models.CharField(choices=COUNTRY, max_length=2)
	age = models.IntegerField(default=0)

	def __str__(self):
	    return self.name

	class Meta:
		verbose_name_plural = 'User Profiles'


class Userratings(models.Model):
    user = models.ForeignKey('auth.User')
    user_review = models.TextField()
    user_ratings = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'User Ratings'