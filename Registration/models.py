from django.db import models

#Creating models for User registration
class Registration(models.Model):
    #for choices to select gender
    #enumeration in python
    class Gender(models.TextChoices):
        Male='male'
        Female='female'
        Hidden='prefer not to say'

    #fieldname,field options and field types for rows and column to store input
    username=models.CharField('username',max_length=150,unique=True)
    gender=models.CharField('gender',max_length=20,choices=Gender.choices)
    phone_number=models.CharField('phone number',max_length=20,unique=True)
    email_addr=models.EmailField('E-mail',unique=True)
    password=models.CharField('password',max_length=200, db_tablespace='pass')
    profile_pic=models.ImageField(upload_to='uploaded',blank=True)

    #defining the manager for this table
    register=models.Manager()
    #using meta class to change the database table name
    class Meta:
        db_table='Registration' #defining the table name

    def __str__(self):
        return self.username
    

#friend class for registering the friends
class Friends(models.Model):
    self_user=models.ForeignKey(Registration,on_delete = models.CASCADE,related_name='friends')
    friend_user=models.ForeignKey(Registration,on_delete = models.CASCADE,related_name='friend')

    class Meta:
        db_table="user_friends"
