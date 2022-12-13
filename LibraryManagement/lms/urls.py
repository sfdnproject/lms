from django.urls import path
from lms import views

urlpatterns = [
    path('addBook/',views.addBook),
    path('viewBook/',views.viewBook),
    path('deleteBook/',views.deleteBook),
    path('returnBook/',views.returnBook),
    path('issueBook/',views.issueBook),
    path('issuedBookList/',views.issuedBookList),
    path('availBook/',views.availBook),
    path('allBook/',views.allBook),
    path('nonFiction/',views.nonFiction),
    path('edited/',views.edited),
    path('reference/',views.reference),
    path('fiction/',views.fiction),
    path('htol',views.highToLow),
    path('ltoh',views.lowToHigh),
    path('atoz',views.atoz),
    path('ztoa',views.ztoa),

    #--------- user profile section----------
    path('userprofile',views.userprofile),
    path('ourbookcollection',views.ourbookcollection),

    path('issuedBookListForUser/',views.issuedBookListForUser),
    path('availBookForUser/',views.availBookForUser),
    path('allBookForUser/',views.allBookForUser),
    path('nonFictionForUser/',views.nonFictionForUser),
    path('editedForUser/',views.editedForUser),
    path('referenceForUser/',views.referenceForUser),
    path('fictionForUser/',views.fictionForUser),
    path('atozbook',views.atozbook),
    path('ztoabook',views.ztoabook),
    path('atozauthor',views.atozauthor),
    path('ztoaauthor',views.ztoaauthor),

]
