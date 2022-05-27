from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group


# Create your views here.
def home(request): # view for homepage
    return render(request, "main/home.html")

def signup_page(request): # view for general signup page
    return render(request, "main/signuppage.html")

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

        if password==password_check:
            if User.objects.filter(username=username).exists():
                print("Username already exists.")
            elif User.objects.filter(email=email).exists():
                print("Email already exists.")
            else:
                user=User.objects.create_user(username=username, password= password, email=email, first_name=fname, last_name=lname)
                user.save()
                print("User created.")
                comp= CompanyTable( 
                    company_name=username,
                    no_of_employees= number_of_employees,
                    phone= phone_no,
                    email=email,
                    address= address,
                    description= description,
                    cap_available= capital_available
                )
                comp.save()
                rep= CompRep(
                    company_id = comp,
                    fname = fname,
                    lname = lname,
                    r_phone = r_phone_no,
                    r_email = r_email

                )
                rep.save()
                
        else:
            print("User not created.")

        return redirect('/')

    else:
        return render(request, "registration/compsignuppage.html")

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
            if User.objects.filter(username=username).exists():
                print("Username already exists.")
            elif User.objects.filter(email=email).exists():
                print("Email already exists.")
            else:
                user=User.objects.create_user(username=username, password= password, email=email, first_name=fname, last_name=lname)
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
                
        else:
            print("User not created.")
        
        return redirect('/')

    else:
        return render(request, "registration/ngosignuppage.html", {})



    


