from django.db import models

# Create your models here.
class movie(models.Model):
	movie_title = models.CharField(max_length=200)
	movie_description = models.CharField(max_length=2000)
	movie_director = models.CharField(max_length=1000)
	movie_year = models.CharField(max_length=6)
	movie_img_href = models.CharField(max_length=4000, default="https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqoNjyoZjeAhXKeX0KHRE2CykQjRx6BAgBEAU&url=http%3A%2F%2Fwww.qygjxz.com%2Fnew-picture.html&psig=AOvVaw2LZeceai3NfLcaShE8ntnE&ust=1540236408049785")

	def __str__(self):
		return movie_title

