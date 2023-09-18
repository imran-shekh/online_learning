from django.db import models



# Create your models here.

class Signup(models.Model):
    first_name = models.CharField(max_length=100, default="", null=True)
    last_name = models.CharField(max_length=100, default="", null=True)
    email = models.CharField(max_length=100, default="", null=True)
    password = models.CharField(max_length=255, default="", null=True)
    age= models.IntegerField( null=True)
    mobile = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=100, default="", null=True)
    
    
    def __str__(self):
        return self.first_name
    
class Course_Details(models.Model):
    course_name = models.CharField(max_length=100, default="", null=True)
    slug = models.CharField(max_length=100, default="", null=True)
    desc = models.CharField(max_length=100, default="", null=True)
    price = models.IntegerField(default=1, null=True)
    discount = models.IntegerField(default=1, null=True)
    course_img = models.ImageField(upload_to = 'static/images/')
    resource = models.FileField(upload_to='resources/course')
    duration = models.TimeField()
    
    def __str__(self):
        return self.course_name
    
    
class Videos(models.Model):
    video_title = models.CharField(max_length= 100, blank=True, null=True)
    video_id = models.CharField(max_length=100, blank=True, null=True)
    video_belong = models.ForeignKey(Course_Details, on_delete=models.CASCADE, default=1)
    video_seq = models.IntegerField(null=True,  blank=True)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.video_title
            

class Course_info(models.Model):
    desc = models.CharField(max_length=300, blank=True, null=True)
    course = models.ForeignKey(Course_Details, on_delete=models.CASCADE)

    class Meta: 
        abstract = True
        
        
class tag(Course_info):
    pass

class  prereq(Course_info):
    pass

class learning(Course_info):
    pass



            
            
            