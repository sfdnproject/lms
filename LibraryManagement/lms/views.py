from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# from lms.forms import RegisterUser
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
from lms.models import Books,BookIssueRecordTable

# Create your views here.


def landing(request):
    return render(request, 'lms/landing.html')


def index(request):
    return render(request, 'lms/index.html')


def addBook(request):
    if (request.method == 'POST'):
        book_name = request.POST['book_name'].title()
        author_name = request.POST['author'].title()
        price = request.POST['price']
        type_of_book = request.POST['tob'].title()

     # create a sql quary to add data into database from form
        insert_data = Books.objects.create(
            book_name=book_name, author_name=author_name, price=price, type_of_book=type_of_book)

        # to execute sql quary
        insert_data.save()

        return redirect('/lms/viewBook')
    return render(request, 'lms/add.html',)


def viewBook(request):
    content = {}
    content['data'] = Books.objects.all()
    return render(request, 'lms/viewBook.html', content)


def deleteBook(request):
    if (request.method == 'POST'):
        b_id = request.POST['b_id']

        book_to_be_deleted = Books.objects.filter(id=b_id)
        book_to_be_deleted.delete()
        return redirect('/lms/viewBook')

    return render(request, 'lms/delete.html')


def returnBook(request):
    if (request.method == 'POST'):
        b_id = request.POST['b_id']
        u_id = request.POST['u_id']
        date_of_issue = request.POST['doi']
        date_of_return = request.POST['dor']


        addToBookIssueRecordTable=BookIssueRecordTable.objects.filter(bookId=b_id, userId=u_id, date_of_issue=date_of_issue)
        addToBookIssueRecordTable.update(status='Return',date_of_return=date_of_return)


        book_to_be_return = Books.objects.filter(id=b_id)
        book_to_be_return.update(status='avail')
        return redirect('/lms/viewBook')

    return render(request, 'lms/return.html')


def issueBook(request):
    if (request.method == 'POST'):
        b_id = request.POST['b_id']
        u_id = request.POST['u_id']
        date_of_issue = request.POST['doi']


        addToBookIssueRecordTable=BookIssueRecordTable.objects.create(bookId=b_id, userId=u_id, date_of_issue=date_of_issue)
        addToBookIssueRecordTable.save()

        book_to_be_issue = Books.objects.filter(id=b_id)
        book_to_be_issue.update(status='issued')
        return redirect('/lms/viewBook')

    return render(request, 'lms/issue.html')

# filter section

def allBook(request):

    content = {}
    content['data'] = Books.objects.all()
    return render(request, 'lms/viewBook.html', content)


def availBook(request):

    content = {}
    content['data'] = Books.objects.filter(status='avail')
    return render(request, 'lms/viewBook.html', content)


def issuedBookList(request):

    content = {}
    content['data'] = Books.objects.filter(status='issued')
    return render(request, 'lms/viewBook.html', content)


def nonFiction(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='non_fiction')
    return render(request, 'lms/viewBook.html', content)


def edited(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='edited')
    return render(request, 'lms/viewBook.html', content)


def reference(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='reference')
    return render(request, 'lms/viewBook.html', content)


def fiction(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='fiction')
    return render(request, 'lms/viewBook.html', content)


def highToLow(request):
    datas = Books.objects.order_by('-price')

    content = {"data": datas}
    return render(request, 'lms/viewBook.html', content)


def lowToHigh(request):
    datas = Books.objects.order_by('price')

    content = {"data": datas}
    return render(request, 'lms/viewBook.html', content)


def atoz(request):
    datas = Books.objects.order_by('author_name')

    content = {"data": datas}
    return render(request, 'lms/viewBook.html', content)


def ztoa(request):
    datas = Books.objects.order_by('-author_name')

    content = {"data": datas}
    return render(request, 'lms/viewBook.html', content)

#-------------admin login---------------------
def superadmin(request):
    if not request.user.is_authenticated:
        messages.warning(request,'please login')
        return redirect('/login')
        # if not request.user.is_superuser:
        #     messages.warning(request,"Please Login By Admin Credentials")
        #     return redirect('/login')
        # else:
        #     return redirect('/index')

    return render(request, 'lms/index.html')

#--------------authuntication section------------------
def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmPassword = request.POST.get("pass2")

        if password != confirmPassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/register')

        if User.objects.filter(username=uname):
            messages.info(request,"username is taken")
            return redirect('/register')

        if User.objects.filter(email=email):
            messages.info(request,"email is taken")
            return redirect('/register')
            
        if len(uname)>10:
            messages.info(request,"username should have less than 10 characters!")
            return redirect('/register')

        myuser = User.objects.create_user(
            username=uname, email=email, password=password, first_name=fname, last_name=lname)

        myuser.save()
        messages.success(request,"Registration Successful Please Login")
        return redirect('/login')

    return render(request, "lms/register.html")


def handlelogin(request):

    if request.method == "POST":
        uname=request.POST['username']
        pass1=request.POST['pass1']
        uid=request.user.id

        myuser = authenticate(username=uname,password=pass1)
        
        if myuser is not None:
            login(request,myuser)
            if request.user.is_superuser:
                messages.success(request,"Login Success")
                return redirect('/index')

            else:
                
                messages.success(request,"Login Success")
                return redirect('lms/userprofile')

        else:
            messages.error(request,"Invalid credentials")
            return redirect('/login')

    return render(request, 'lms/login.html')

def handlelogout(request):
    logout(request)
    return redirect('/')

# ---------------user section------------------

def userprofile(request):
    content={}
    uid=request.user.id
    fname=request.user.first_name
    lname=request.user.last_name
    username=request.user.username
    email=request.user.email

    content["data"]= BookIssueRecordTable.objects.filter(userId=uid)
    content["fname"]=fname
    content["lname"]=lname
    content["username"]=username
    content["email"]=email

    mydata=content['data'].values_list("bookId")
   
    # print(content['data'].values())
    # print(mydata)
    bookIds=[]
    for i in mydata:
        for j in i:
            bookIds.append(j)
    # print(bookIds)
    
    book_author=[]

    for i in bookIds:
        bookAndAuthorName=Books.objects.filter(id=i)
        bookAndAuthorName=bookAndAuthorName.values_list('book_name','author_name','type_of_book')
        # print(bookAndAuthorName)
        for j in bookAndAuthorName:
            for k in j:
                book_author.append(k)
                    
            # print(f'BookName:{book_author[0]}\nAuthorName:{book_author[1]}')
            # s['book_name']=book_author[0]
            # s['author_name']=book_author[1]
    # print(book_author)

    chek_data=content['data'].values()
    cont={}
    list_new=[]
    for data in chek_data:
        # s['cheking']='ok'
        # print(s)
        data['book_name']=book_author[0]
        data['author_name']=book_author[1]
        data['type_of_book']=book_author[2]
        book_author.pop(0) 
        book_author.pop(0) 
        book_author.pop(0) 
        # print(book_author)
        list_new.append(data)
        # print(content)
    # print(list_new)
    cont["data"]=list_new
    cont["fname"]=fname
    cont["lname"]=lname
    cont["username"]=username
    cont["email"]=email
    # print(cont)
    return render(request,'lms/userprofile.html',cont)

def ourbookcollection(request):
    content = {}
    content['data'] = Books.objects.all()
    return render(request,'lms/bookcollection.html',content)

# ----------------Filter section for userprofile page -------------

def allBookForUser(request):

    content = {}
    content['data'] = Books.objects.all()
    return render(request, 'lms/bookcollection.html', content)


def availBookForUser(request):

    content = {}
    content['data'] = Books.objects.filter(status='avail')
    return render(request, 'lms/bookcollection.html', content)


def issuedBookListForUser(request):

    content = {}
    content['data'] = Books.objects.filter(status='issued')
    return render(request, 'lms/bookcollection.html', content)


def nonFictionForUser(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='non_fiction')
    return render(request, 'lms/bookcollection.html', content)


def editedForUser(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='edited')
    return render(request, 'lms/bookcollection.html', content)


def referenceForUser(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='reference')
    return render(request, 'lms/bookcollection.html', content)


def fictionForUser(request):
    content = {}
    content['data'] = Books.objects.filter(type_of_book='fiction')
    return render(request, 'lms/bookcollection.html', content)


def atozbook(request):
    datas = Books.objects.order_by('book_name')

    content = {"data": datas}
    return render(request, 'lms/bookcollection.html', content)


def ztoabook(request):
    datas = Books.objects.order_by('-book_name')

    content = {"data": datas}
    return render(request, 'lms/bookcollection.html', content)


def atozauthor(request):
    datas = Books.objects.order_by('author_name')

    content = {"data": datas}
    return render(request, 'lms/bookcollection.html', content)


def ztoaauthor(request):
    datas = Books.objects.order_by('-author_name')

    content = {"data": datas}
    return render(request, 'lms/bookcollection.html', content)
