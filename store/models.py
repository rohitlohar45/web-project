from django import forms
from django.db import models

from users.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Supplier(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    contact = models.CharField(max_length=20)
    mob_no = PhoneNumberField(region="IN")
    email = models.EmailField(max_length=120)
    ename = models.CharField(max_length=120)
    econtact = models.CharField(max_length=120)
    emob_no = PhoneNumberField(region="IN")
    eemail = models.EmailField(max_length=120)
    

    def __str__(self):
        return self.name


    


class Yard(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name        



class cost(models.Model):
    name = models.CharField(max_length=120)
    shortform = models.CharField(max_length=120)
    rate = models.IntegerField()
    misc = models.CharField(max_length=120)

    def __str__(self):
        return self.name  




class metal(models.Model):
    name = models.CharField(max_length=120)
    shortform = models.CharField(max_length=120)
    rate = models.IntegerField()
    misc = models.CharField(max_length=120)

    def __str__(self):
        return self.name  

class Typeo(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

CHOICES = tuple(metal.objects.values_list('shortform','shortform'))
CHOICES1 =  tuple(cost.objects.values_list('name','name'))

# CHOICES10 = cost.objects.values_list('id','rate')
# dict = forms.model_to_dict(cost)
# print(dict)

name2 = "Clearing Housing agency"



# print(CHOICES10)   


# print(value(name).values('rate'))    

class grade(models.Model):
    name = models.CharField(max_length=120)
    details = models.CharField(max_length=120)
    gradegrp = models.CharField(max_length=120)
    misc = models.CharField(max_length=120)
    metaln =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalnn =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    # print(cost.objects.values_list(metaln, flat=True))
    metalc = models.IntegerField(default=0)
    
    metalcn = models.IntegerField(default=0)
    metaln1 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc1 = models.IntegerField(default=0)
    metaln2 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc2 = models.IntegerField(default=0)
    metaln3 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc3 = models.IntegerField(default=0)
    metaln4 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc4 = models.IntegerField(default=0)
    metaln5 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc5 = models.IntegerField(default=0)
    metaln6 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc6 = models.IntegerField(default=0)
    metaln7 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc7 = models.IntegerField(default=0)
    metaln8 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc8 = models.IntegerField(default=0)
    metaln9 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc9 = models.IntegerField(default=0)
    metaln10 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc10 = models.IntegerField(default=0)
    metaln11 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc11 = models.IntegerField(default=0)
    metaln12 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc12 = models.IntegerField(default=0)
    metaln13 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc13 = models.IntegerField(default=0)
    metaln14 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc14 = models.IntegerField(default=0)
    metaln15 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc15 = models.IntegerField(default=0)
    metaln16 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc16 = models.IntegerField(default=0)
    metaln17 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc17 = models.IntegerField(default=0)
    metaln18 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc18 = models.IntegerField(default=0)
    metaln19 =models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc19 = models.IntegerField(default=0)
    metaln20 = models.CharField(max_length=120, choices=CHOICES, default=CHOICES1[0], null=True )
    metalc20 = models.IntegerField(default=0)
    
    costn =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    

    costnn =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc = models.IntegerField(default=0)
    costcn = models.IntegerField(default=0)
    costn1 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc1 = models.IntegerField(default=0)
    costn2 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc2 = models.IntegerField(default=0)
    costn3 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc3 = models.IntegerField(default=0)
    costn4 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc4 = models.IntegerField(default=0)
    costn5 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc5 = models.IntegerField(default=0)
    costn6 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc6 = models.IntegerField(default=0)
    costn7 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc7 = models.IntegerField(default=0)
    costn8 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc8 = models.IntegerField(default=0)
    costn9 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc9 = models.IntegerField(default=0)
    costn10 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc10 = models.IntegerField(default=0)
    costn11 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc11 = models.IntegerField(default=0)
    costn12 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc12 = models.IntegerField(default=0)
    costn13 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc13 = models.IntegerField(default=0)
    costn14 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc14 = models.IntegerField(default=0)
    costn15 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc15 = models.IntegerField(default=0)
    costn16 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc16 = models.IntegerField(default=0)
    costn17 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc17 = models.IntegerField(default=0)
    costn18 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc18 = models.IntegerField(default=0)
    costn19 =models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc19 = models.IntegerField(default=0)
    costn20 = models.CharField(max_length=120, choices=CHOICES1, default=CHOICES1[0], null=True )
    costc20 = models.IntegerField(default=0)
    recovery = models.CharField(max_length=120)
    typeo = models.ForeignKey(Typeo,on_delete=models.CASCADE)
    
    
    # costc = models.IntegerField()

    def __str__(self):
        return self.name  

