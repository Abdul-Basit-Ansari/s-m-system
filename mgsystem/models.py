from django.db import models
from django.contrib.auth.models import User
# from django.forms import DateTimeField
from django.utils.timezone import now
# Create your models here.

# class Mguser(models.Model):
# 	"""Model definition for Mguser."""
# 	sno=models.AutoField(primary_key=True)
# 	fname = models.CharField(max_length=50)
# 	lname = models.CharField(max_length=50)
# 	uname = models.CharField(max_length=50)
# 	phone = models.IntegerField()
# 	email = models.EmailField()
# 	password = models.CharField(max_length=50)
# 	class Meta:
# 		"""Meta definition for Mguser."""

# 		verbose_name = 'Mguser'
# 		verbose_name_plural = 'Mgusers'

# 	def __str__(self):
# 		"""Unicode representation of Mguser."""
# 		return self.fname + self.lname



class Mgdata(models.Model):
	"""Model definition for Mgdata."""
	sno = models.AutoField(primary_key=True)
	img = models.ImageField(upload_to="studentsimg")
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	father = models.CharField(max_length=50)
	phone = models.BigIntegerField()
	email = models.EmailField(max_length=100)
	stuclass = models.IntegerField()
	section=models.CharField(max_length=3 , default="A" )
	jiontime = models.DateTimeField(auto_now_add=True) 
	isdelete = models.BooleanField(default=False) 
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	# class Meta:
	# 	"""Meta definition for Mgdata."""

	# 	model = Mgdata
	# 	field = '__all__'

	def __str__(self):
		"""Unicode representation of Mgdata."""
		return f"{self.user.username} : {self.fname} {self.lname}"


class Report(models.Model):
	"""Model definition for Report."""
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	rep = models.TextField()
	
	
	def __str__(self):
		"""Unicode representation of Report."""
		return self.name

class Contactus(models.Model):
	"""Model definition for Contactus."""
	sno=models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField()
	desc = models.TextField()
	

	def __str__(self):
		"""Unicode representation of Contactus."""
		return self.name
