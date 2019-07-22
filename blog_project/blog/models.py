from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
	)

	body = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])

class Product(models.Model):
	prod_id = models.IntegerField()
	director = models.CharField(max_length=15)
	producer = models.CharField(max_length=15)
	actor = models.CharField(max_length=10)
	title = models.CharField(max_length=15)

	class Meta:
		indexes = [
			models.Index(fields=['prod_id']),
			models.Index(fields=['actor']),
			models.Index(fields=['director', 'producer'])
		]

class Company(models.Model):
	name = models.CharField(max_length=30)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Sport(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=30)
	courses = models.ManyToManyField(
		Course,
		blank=True,
		through='StudentCourses'
	)
	sports = models.ManyToManyField(
		Sport,
		blank=True,
		through='StudentSports'
	)

	def __str__(self):
		return self.name

class StudentCourses(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.course.name

class StudentSports(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

	def __str__(self):
		return self.sport.name
