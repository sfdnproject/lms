from django.db import models

# Create your models here.

class Books(models.Model):

    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    type_of_book=models.CharField(max_length=100)
    status=models.CharField(max_length=10,default='avail')
    is_deleted=models.CharField(max_length=5,default='n')
    

class BookIssueRecordTable(models.Model):
    bookId=models.IntegerField()
    userId=models.IntegerField()
    date_of_issue=models.DateField()
    date_of_return=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=15,default='Taken')

# class Students(models.Model):
#     stud_name=models.CharField(max_length=50)

