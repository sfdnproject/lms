from django.contrib import admin
from lms.models import Books,BookIssueRecordTable

# Register your models here.
class BooksTableAdmin(admin.ModelAdmin):
    list_display=['id','book_name','author_name','price','type_of_book','status']
admin.site.register(Books,BooksTableAdmin)


class BookIssueRecordTableAdmin(admin.ModelAdmin):
    list_display=['id','bookId','userId','date_of_issue','date_of_return','status']
admin.site.register(BookIssueRecordTable,BookIssueRecordTableAdmin)
