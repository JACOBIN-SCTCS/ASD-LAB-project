from django.db import models
import datetime
# Create your models here.


PRIORITY_CHOICES=(
    (1,1),(2,2) , (3,3) ,(4,4) , (5,5)
)


#THE FOLLOWING IS USED TO STORE THE SCHEMA OF THE TABLE THAT WE ARE USING
class Todo(models.Model):
    todo_id=models.AutoField(primary_key=True)  # AUTOMATICALLY INCREMENTED
    todo_desc=models.CharField(max_length=40)   # THE DESCRIPTION OF TODOS
    due_date=models.DateTimeField(default=datetime.datetime.now()) #DATE TO BE COMPLETED DATE TIME FIELD
    priority=models.IntegerField(default=1,choices=PRIORITY_CHOICES) #PRIORITY AN INTEGER
    completed=models.BooleanField(default=False)




    