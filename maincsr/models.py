from django.db import models

# Create your models here.
class CompanyTable(models.Model):
    company_name=models.CharField(max_length=256)
    passwd = models.CharField(max_length=32)
    no_of_employees= models.IntegerField()
    phone= models.BigIntegerField()
    email= models.EmailField()
    address= models.TextField()
    description= models.TextField()
    activity_status=models.BooleanField()
    total_amount_donated= models.BigIntegerField()
    cap_available= models.BigIntegerField()


    def __str__(self):
        return self.company_name


class NGOTable(models.Model):
    ngo_name = models.CharField(max_length=256)
    passwd = models.CharField(max_length = 32)
    no_of_employees= models.IntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    description= models.TextField()
    activity_status = models.BooleanField()
    total_recd = models.BigIntegerField()
    min_cap_reqd = models.BigIntegerField()

    def __str__(self):
        return self.ngo_name

class CompRep(models.Model):
    company_id=models.ForeignKey(CompanyTable, on_delete=models.CASCADE)
    #passwd = models.ForeignKey(NGOTable, on_delete = models.CASCADE)
    fname=models.CharField(max_length=256)
    lname=models.CharField(max_length=256)
    phone = models.BigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.fname} {self.lname}"


class NGORep(models.Model):
    ngo_id = models.ForeignKey(NGOTable, on_delete = models.CASCADE)
    #passwd = models.ForeignKey(NGOTable.passwd, on_delete = models.CASCADE)
    fname = models.CharField(max_length=256)
    lname = models.CharField(max_length=256)
    phone = models.BigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

# class TransacHist(models.Model):
#     company_id=models.ForeignKey(CompanyTable.company_id, on_delete=models.CASCADE)
#     ngo_id = models.ForeignKey(NGOTable.ngo_id, on_delete = models.CASCADE)

#     transacamt = models.