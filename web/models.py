from django.db import models

# Create your models here.


class Popular_Courses(models.Model):
  image = models.ImageField(upload_to='media')
  name = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)
  name_two = models.CharField(max_length=100)
  students = models.CharField(max_length=50)
  lessons = models.CharField(max_length=50)
  fees = models.CharField(max_length=50)

  lectures = models.IntegerField()
  duration = models.CharField(max_length=20)
  student = models.IntegerField()


  first_content = models.CharField(max_length=500)
  second_content = models.CharField(max_length=500)
  topic_one = models.CharField(max_length=100) 
  topic_two = models.CharField(max_length=100)
  topic_three = models.CharField(max_length=100)
  topic_four = models.CharField(max_length=100)
  topic_five = models.CharField(max_length=100)
  topic_six = models.CharField(max_length=100)
  topic_seven = models.CharField(max_length=100)
  topic_eight = models.CharField(max_length=100)
  requirement_one = models.CharField(max_length=200)
  requirement_two = models.CharField(max_length=200)
  requirement_three = models.CharField(max_length=200)
  requirement_four = models.CharField(max_length=200)
  requirement_five = models.CharField(max_length=200)
  

  def __str__(self):
      return self.name
  

class Top_Subjects(models.Model):
  icon = models.ImageField(upload_to='media')
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=500)


class Events(models.Model):
   image = models.ImageField(upload_to='media')
   location = models.CharField(max_length=100)
   time = models.TimeField()
   title = models.CharField(max_length=200)
   date = models.DateField()

   def __str__(self):
       return self.title
   


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)  
    
  
class CoursesEnquirys(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()
    def __str__(self):
        return str(self.name)  
    
class EventsRegister(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()
    def __str__(self):
        return str(self.name)  
    
class Testimonial(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    