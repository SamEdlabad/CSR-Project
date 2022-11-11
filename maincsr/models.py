from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class CompanyTable(models.Model):
    company_name=models.CharField(max_length=256, unique=True)
    #passwd = models.CharField(max_length=32)
    no_of_employees= models.IntegerField()
    phone = models.CharField(max_length=20,null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    email= models.EmailField(unique=True)
    address= models.TextField()
    description= models.TextField()
    activity_status=models.BooleanField(default=True)
    total_amount_donated= models.BigIntegerField(default=0)
    cap_available= models.BigIntegerField()


    def __str__(self):
        return self.company_name


class NGOTable(models.Model):
    regis_num=models.CharField(max_length=256,null=True) #new
    state=models.CharField(max_length=256,null=True) #new
    district=models.CharField(max_length=256,null=True) #new
    ngo_name = models.CharField(max_length=256, unique=True)
    #passwd = models.CharField(max_length = 32)
    pdf=models.FileField(null=True) #new- anshuman has added
    no_of_employees= models.IntegerField(null=True)
    phone = models.CharField(max_length=20,null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    email = models.EmailField(unique=True)
    address = models.TextField()
    description= models.TextField()
    activity_status = models.BooleanField(default=True)
    total_recd = models.BigIntegerField(default=0)
    min_cap_reqd = models.BigIntegerField(null=True)
    sectors=models.TextField(max_length=512,null=True) #Textfield can store more than 256 characters
    #new
    website=models.CharField(max_length=256,null=True) #new


    def __str__(self):
        return self.ngo_name

class CompRep(models.Model):
    company_id=models.ForeignKey(CompanyTable, on_delete=models.CASCADE)
    #passwd = models.ForeignKey(NGOTable, on_delete = models.CASCADE)
    fname=models.CharField(max_length=256)
    lname=models.CharField(max_length=256)
    r_phone = models.CharField(max_length=20,null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    r_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class NGORep(models.Model):
    ngo_id = models.ForeignKey(NGOTable, on_delete = models.CASCADE)
    #passwd = models.ForeignKey(NGOTable.passwd, on_delete = models.CASCADE)
    fname = models.CharField(max_length=256,null=True)
    lname = models.CharField(max_length=256,null=True)
    r_phone = models.CharField(max_length=20,null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    r_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Connections(models.Model):
    connid=models.AutoField(primary_key=True)
    ngo_name = models.CharField(max_length=256)
    company_name=models.CharField(max_length=256)
    initiator=models.CharField(max_length=256)
    status=models.CharField(max_length=20)
    respdate=models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    senddate=models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"{self.ngo_name} {self.company_name}"
