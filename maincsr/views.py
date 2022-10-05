from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages #to display error messages
from django.urls import reverse
import time
#from validate_email import validate_email#for email validation
from django.conf import settings
from django.core.mail import send_mail
import snoop

@snoop
def mail(subject, message, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,recipient_list,fail_silently=True)

def search(request):
    cat = request.POST['category']#'NGO'
    orgname = request.POST['orgname']#'He'
    emp_count = request.POST['emp_count']#500
    cap = int(request.POST['cap'])#85000
    state = request.POST['state']
    sector = request.POST['sector']
    sort_by = request.POST['sort_by']#'ngo_name' or 'company_name'
    order = request.POST['order']
    if cat == 'NGO':
        data = NGOTable.objects.filter(ngo_name__icontains = orgname,)# i here makes it non case sensitive
        if cap != 0:
            data = data.filter(min_cap_reqd__range = (cap,cap + 10000))
    elif cat == 'COMPANY':
        data = CompanyTable.objects.filter(company_name__icontains = orgname)
        if cap != 0:
            data = data.filter(cap_available__range = (cap ,cap + 10000))

    if emp_count != 'None':
        emp_count = int(emp_count)
        data = data.filter(no_of_employees__range = (emp_count - 500,emp_count + 500))# range is the between and 
    if state != 'None':
        data = data.filter(state__exact = state)#exact as the name suggests means exact value
    if sector != 'None':
        data = data.filter(sectors__in = sector)
    if sort_by != 'None':
        if order  == 'ascending':
            data = data.order_by(sort_by)
        elif order == 'descending':
            sort_by = '-'+sort_by
            data = data.order_by(sort_by)

def EMAILCHECK(Email):
    return True#validate_email(Email,verify=True)

attempts=0#no of attempts made
WAIT=False#Condition that indicates whether if the User is to wait

# Create your views here.
def home(request): # view for homepage
    return render(request, "main/home.html")

def signup_page(request): # view for general signup page
    return render(request, "main/signuppage.html")

@snoop
def company_signup_page(request): # view for copany signup page
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        password_check= request.POST['password_check']
        number_of_employees= request.POST['number_of_employees']
        capital_available= request.POST['capital_available']
        phone_no= request.POST['phone_no']
        email= request.POST['email']
        address= request.POST['address']
        description= request.POST['description']
        fname= request.POST['fname']
        lname= request.POST['lname ']
        r_email= request.POST['r_email ']
        r_phone_no= request.POST['r_phone_no ']

        if password==password_check: #to check if confirm password option works
            if len(password) < 5:                #to check password length
                messages.info(request, "Password too short. Atleast 5 characters are required.")
                return redirect('/Company-sign-up-page')
            elif len(password) > 50:             #to check password length
                messages.info(request, "Password too long. Atmost 50 characters are required.")
                return redirect('/Company-sign-up-page')
            elif User.objects.filter(username=username).exists(): #to check if the username already exists
                messages.info(request, "Username taken.")
                return redirect('/Company-sign-up-page')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Company Email taken.")
                return redirect('/Company-sign-up-page')
            elif CompRep.objects.filter(r_email=r_email).exists():
                messages.info(request, "Representative email taken.")
                return redirect('/Company-sign-up-page')
            elif not EMAILCHECK(email):
                messages.info(request, "Company Email invalid.")
                return redirect('/Company-sign-up-page')
            elif not EMAILCHECK(r_email):
                messages.info(request, "Representative email invalid.")
                return redirect('/Company-sign-up-page')
            else:
                user=User.objects.create_user(username=username, password= password, email=email, first_name=fname, last_name=lname) #default table created django
                user.save()
                comp= CompanyTable( #storing the appropriate details in company table
                    company_name=username,
                    no_of_employees= number_of_employees,
                    phone=phone_no,
                    email=email,
                    address= address,
                    description= description,
                    cap_available= capital_available
                )
                comp.save()
                rep= CompRep( #storing the appropriate details in representative table
                    company_id = comp,
                    fname = fname,
                    lname = lname,
                    r_phone = r_phone_no,
                    r_email = r_email

                )
                rep.save()

                subject = "Registration has been completed."
                msg1 = "Hello "+username+"!!!,\nThank you for creating an account on our Platform. \n\nWe look forward to seeing your generosity."
                msg2 = "\nHope you find it easy to find the right charity.\n--The CSR Platform Team."
                message = msg1+msg2
                recipient_list = [email,r_email]
                mail(subject,message,recipient_list)
        else:
            messages.info(request, "Passwords not matching.") #returns error message
            return redirect('/Company-sign-up-page')

        return redirect('/login')

    else:
        return render(request, "registration/compsignuppage.html")

@snoop
def ngo_signup_page(request): # view for ngo signup page
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        password_check= request.POST['password_check']
        number_of_employees= request.POST['number_of_employees']
        capital_reqd= request.POST['capital_reqd']
        phone_no= request.POST['phone_no']
        email= request.POST['email']
        address= request.POST['address']
        description= request.POST['description']
        fname= request.POST['fname']
        lname= request.POST['lname ']
        r_email= request.POST['r_email ']
        r_phone_no= request.POST['r_phone_no ']

        if password==password_check:
            if len(password) < 5:      #to check password length
                messages.info(request, "Password too short. At least 5 characters are required.")
                return redirect('/NGO-sign-up-page')
            elif len(password) > 50:   #to check password length
                messages.info(request, "Password too long. At most 50 characters are required.")
                return redirect('/NGO-sign-up-page')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username taken.")
                return redirect('/NGO-sign-up-page')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "NGO Email taken.")
                return redirect('/NGO-sign-up-page')
            elif NGORep.objects.filter(r_email=r_email).exists():
                messages.info(request, "Representative email taken.")
                return redirect('/Company-sign-up-page')
            elif not EMAILCHECK(email):
                messages.info(request, "NGO Email invalid.")
                return redirect('/Company-sign-up-page')
            elif not EMAILCHECK(r_email):
                messages.info(request, "Representative email invalid.")
                return redirect('/Company-sign-up-page')
            else:
                user=User.objects.create_user(username=username, password= password , email=email, first_name=fname, last_name=lname) #password will be hashed in table
                user.save()
                print("User created.")
                ngo= NGOTable( 
                    ngo_name=username,
                    no_of_employees= number_of_employees,
                    phone= phone_no,
                    email=email,
                    address= address,
                    description= description,
                    min_cap_reqd= capital_reqd
                )
                ngo.save()
                rep= NGORep(
                    ngo_id = ngo,
                    fname = fname,
                    lname = lname,
                    r_phone = r_phone_no,
                    r_email = r_email

                )
                rep.save()
                subject = 'Registration completed Sucessfully'
                msg1 = 'Hello'+username+'!!!,\nThank you for creating an account with our Platform.'
                msg2 = '\n\nWe look forward to seeing you help everyone.\n--The CSR Platform Team'
                message = msg1 + msg2
                recipient_list = [email,r_email]
                mail(subject,message,recipient_list)
        else:
            messages.info(request, "Passwords not matching.") #returns error message
            return redirect('/NGO-sign-up-page')
        
        return redirect('/login')

    else:
        return render(request, "registration/ngosignuppage.html")



def login(request):
    global WAIT,attempts
    if WAIT==True:#If the user is to be made to wait, a timer for 30 seconds is set while the user is denied any controls
        time.sleep(30)#Become inactive for 30 secs
        WAIT=False;attempts=0
        return render(request,"registration/login.html",{"WAIT":False})
    if request.method=='POST':
        attempts+=1
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username,password=password) #default django authentication protocol that we are calling
        if user is not None:
            auth.login(request,user) #django function allows you to log in
            return redirect(f"/dashboard/{username}")
            attempts=0

        else:
            if attempts>=3: #If more than 3 attempts are made, the user's panel is frozen for 30 seconds
                messages.info(request,"You have exceeded 3 attempts of logging in. Please hit refresh and wait for 30 seconds")
                WAIT=True
                return render(request,"registration/login.html",{'WAIT':True})
   

            messages.info(request, "Username or password is incorrect.")
            return redirect("/login")
    else:
        return render(request, "registration/login.html")


def dashboard(request, username):
    users=[]
    try:
        data= CompanyTable.objects.get(company_name=username)
        odt = NGOTable.objects.values_list('ngo_name',flat=True)
        for user in odt:
            users.append(user)
        return render(request, "main/dashboard.html", {'about': data.description,
        'email': data.email,
        'phone': data.phone,
        'address': data.address,
        'users': users,
        'org_name': username
        })
    except:
        data= NGOTable.objects.get(ngo_name=username)
        odt = CompanyTable.objects.values_list('company_name',flat=True)
        for user in odt:
            users.append(user)
        return render(request, "main/dashboard.html", {'about': data.description,
        'email': data.email,
        'phone': data.phone,
        'address': data.address,
        'users': users,
        'org_name': username 
        })

def logout(request):
    auth.logout(request)#default django logout function
    return redirect('')

@snoop
def connect(request):
    org_name = request.POST.get('user')
    connect_with = request.POST.get('connect_with')
    return HttpResponse('User will be sent a connection mail.')