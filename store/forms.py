from cProfile import label
from dataclasses import fields
from email.policy import default
from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin

from store.models import Quality, Supplier, Yard, metal, cost, grade


class SupplierForm(forms.ModelForm):
    mob_no = forms.CharField(label='Mobile Number',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'mob_no',}))
    emob_no = forms.CharField(label='Mobile Number',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'emob_no',}))
    ename = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ename',}))
    econtact = forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'contact',}))
    eemail = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'eemail',}))
    class Meta:
        model = Supplier
        fields = "__all__"
        # fields = [
        #     'name', 'address','contact','mob_no','email','ename','econtact','emob_no','eemail'
        # ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'contact'
            }),
            # 'mob_no': forms.TextInput(attrs={
            #     'class': 'form-control', 'id': 'mob_no',
            # }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'ename': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'ename'
            }),
            'econtact': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'econtact'
            }),
            'emob_no': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'emob_no'
            }),
            'eemail': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'eemail'
            }),
        }

        def __init__(self,*args,**kwargs):
            super(SupplierForm,self).__init__(*args,**kwargs)
            self.fields['ename'].label = "Name"
    # contact = models.CharField(max_length=20)
    # mob_no = models.CharField(max_length=20)
    # email = models.CharField(max_length=50)
    # ename = models.CharField(max_length=120)
    # econtact = models.CharField(max_length=120)
    # emob_no = models.CharField(max_length=120)
    # eemail = models.CharField(max_length=120)
    # supp_id = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'id': 'supp_id',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter supplier id',
    # }))

    # def clean(self):
    #     self.add_error('supp_id', "ID Already exists")


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name', 'address','contact','mob_no','email','ename','econtact','emob_no','eemail'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'contact'
            }),
            'mob_no': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'mob_no'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'ename': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'ename'
            }),
            'econtact': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'econtact'
            }),
            'emob_no': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'emob_no'
            }),
            'eemail': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'eemail'
            }),
        }
   


class YardForm(forms.ModelForm):
    class Meta:
        model = Yard
        fields = [
            'name', 'address'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
        }


class YardUpdateForm(forms.ModelForm):
    class Meta:
        model = Yard
        fields = [
            'supplier','name', 'address'
        ]
        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
        }        



# class OverheadCostForm(forms.ModelForm):
#     class Meta:
#         model = OverheadCost
#         fields = [
#             'yard','name', 'cost'
#         ]

#         widgets = {
#             'yard': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'yard'
#             }),
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'name'
#             }),
#             'cost': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'cost'
#             }),
#         }


       


class MetalForm(forms.ModelForm):
    class Meta:
        model = metal
        fields = [
            'name','shortform','misc'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'shortform': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'shortform'
            }),
            'misc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'misc'
            })
        }

class MetalUpdateform(forms.ModelForm):
    class Meta:
        model = metal

        fields = [
            'name','shortform','misc'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'shortform': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'shortform'
            }),
            'misc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'misc'
            })
        }




class CostForm(forms.ModelForm):
    class Meta:
        model = cost
        fields = [
            'name','shortform','rate','misc'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'shortform': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'shortform'
            }),
            'rate': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'rate'
            }),
            'misc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'misc'
            })
        }

class CostUpdateform(forms.ModelForm):
    class Meta:
        model = cost

        fields = [
            'name','shortform','rate','misc'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'shortform': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'shortform'
            }),
            'rate': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'rate'
            }),
            'misc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'misc'
            })
        }
        
            

def value(name):
    c = cost.objects.filter(
        name__startswith=name).values('rate')
    # print(c.values('rate'))
    # print(c)
    return c 

   

   

# quer = forms.model_to_dict(cost)
# que = tuple(cost.objects.values_list('name','rate'))
# print(quer["Clearing Housing agency"])
# quer = cost.objects.values_list('name','rate')

# MODEL_CHOICES=cost.objects.values_list('name','rate')
# print(MODEL_CHOICES)

MODEL_CHOICES = {
    'Clearing Housing agency': 500
}


# print(MODEL_CHOICES['Clearing Housing agency'])

class GradeForm(forms.ModelForm):
    class Meta:
        model = grade
        
        fields = [
            'name','details','gradegrp','misc','metalc','costc','metaln','typeo','recovery','metalcn','metalnn',
            'metaln1','metalc1','metaln2','metalc2','metaln3','metalc3','metaln4','metalc4','metaln5','metalc5',
            'metaln6','metalc6','metaln7','metalc7','metaln8','metalc8','metaln9','metalc9','metaln10','metalc10',
            'metaln11','metalc11','metaln12','metalc12','metaln13','metalc13','metaln14','metalc14','metaln15','metalc15',
            'metaln16','metalc16','metaln17','metalc17','metaln18','metalc18','metaln19','metalc19','metaln20','metalc20',
            'costcn','costnn','costn',
            'costn1','costc1','costn2','costc2','costn3','costc3','costn4','costc4','costn5','costc5',
            'costn6','costc6','costn7','costc7','costn8','costc8','costn9','costc9','costn10','costc10',
            'costn11','costc11','costn12','costc12','costn13','costc13','costn14','costc14','costn15','costc15',
            'costn16','costc16','costn17','costc17','costn18','costc18','costn19','costc19','costn20','costc20'
        ]
        # costn = forms.Select(attrs={
        #         'class': 'form-control col', 'id': 'costn',
        # }),
        # costc = DynamicField(
        #         forms.IntegerField,
        #         inital=lambda form: form.MODEL_CHOICES[form["costn"].value()],
                
        # ),
        metaln = forms.ChoiceField()

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'details': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'details'
            }),
            'gradegrp': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'gradegrp'
            }),
            'misc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'misc'
            }),
            'metaln': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln'
            }),
            
            
            'metalnn': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metalnn',
            }),
            'costnn': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costnn',
            }),
            'costcn': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costcn',
            }),
            'metalc': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc',
            }),
            'costn' : forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn',
            }),
            'metalcn': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalcn',
            }),
            'costc': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc',
            }),
            'metaln1': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln1',
            }),
            'metalc1': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc1',
            }),
            'metaln2': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln2',
            }),
            'metalc2': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc2',
            }),
            'metaln3': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln3',
            }),
            'metalc3': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc3',
            }),
            'metaln4': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln4',
            }),
            'metalc4': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc4',
            }),
            'metaln5': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln5', 
            }),
            'metalc5': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc5',
            }),
            'metaln6': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln6',
            }),
            'metalc6': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc6',
            }),
            'metaln7': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln7',
            }),
            'metalc7': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc7',
            }),
            'metaln8': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln8',
            }),
            'metalc8': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc8',
            }),
            'metaln9': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln9',
            }),
            'metalc9': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc9',
            }),
            'metaln10': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln10',
            }),
            'metalc10': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc10',
            }),
            'metaln11': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln11',
            }),
            'metalc11': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc11',
            }),
            'metaln12': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln12',
            }),
            'metalc12': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc12',
            }),
            'metaln13': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln13',
            }),
            'metalc13': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc13',
            }),
            'metaln14': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln14',
            }),
            'metalc14': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc14',
            }),
            'metaln15': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln15',
            }),
            'metalc15': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc15',
            }),
            'metaln16': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln16',
            }),
            'metalc16': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc16',
            }),
            'metaln17': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln17',
            }),
            'metalc17': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc17',
            }),
            'metaln18': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln18',
            }),
            'metalc18': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc18',
            }),
            'metaln19': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln19',
            }),
            'metalc19': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc19',
            }),
            'metaln20': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln20',
            }),
            'metalc20': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc20',
            }),
            'costn1': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn1',
            }),
            'costc1': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc1',
            }),
            'costn2': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn2',
            }),
            'costc2': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc2',
            }),
            'costn3': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn3',
            }),
            'costc3': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc3',
            }),
            'costn4': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn4',
            }),
            'costc4': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc4',
            }),
            'costn5': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn5',
            }),
            'costc5': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc5',
            }),
            'costn6': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn6',
            }),
            'costc6': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc6',
            }),
            'costn7': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn7',
            }),
            'costc7': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc7',
            }),
            'costn8': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn8',
            }),
            'costc8': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc8',
            }),
            'costn9': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn9',
            }),
            'costc9': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc9',
            }),
            'costn10': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn10',
            }),
            'costc10': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc10',
            }),
            'costn11': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn11',
            }),
            'costc11': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc11',
            }),
            'costn12': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn12',
            }),
            'costc12': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc12',
            }),
            'costn13': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn13',
            }),
            'costc13': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc13',
            }),
            'costn14': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn14',
            }),
            'costc14': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc14',
            }),
            'costn15': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn15',
            }),
            'costc15': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc15',
            }),
            'costn16': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn16',
            }),
            'costc16': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc16',
            }),
            'costn17': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn17',
            }),
            'costc17': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc17',
            }),
            'costn18': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn18',
            }),
            'costc18': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc18',
            }),
            'costn19': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn19',
            }),
            'costc19': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc19',
            }),
            'costn20': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn20',
            }),
            'costc20': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc20',
            }),



            
            'typeo': forms.Select(attrs={
                'class': 'form-control col', 'id': 'typeo'
            }),
            'recovery': forms.TextInput(attrs={
                'class': 'form-control col', 'id': 'recovery'
            }),

        } 

    # def get_form_kwargs(self):
    #     kwargs = super(self).get_form_kwargs()
    #     kwargs['use_required_attribute'] = False
    #     return kwargs    
    
    def __init__(self, *args, **kwargs):
        super(GradeForm, self).__init__(*args,**kwargs)
        self.fields['costn'].label = 'Select'
        self.fields['costn'].label = None
        self.fields['costn1'].empty_label = None
        self.fields['costn2'].required = False
        self.fields['costn3'].required = False



class GradeUpdateform(forms.ModelForm):
    class Meta:
        model = grade
        fields = [
            'name','details','gradegrp','misc','metalc','costc','metaln','typeo','recovery','metalcn','metalnn',
            'metaln1','metalc1','metaln2','metalc2','metaln3','metalc3','metaln4','metalc4','metaln5','metalc5',
            'metaln6','metalc6','metaln7','metalc7','metaln8','metalc8','metaln9','metalc9','metaln10','metalc10',
            'metaln11','metalc11','metaln12','metalc12','metaln13','metalc13','metaln14','metalc14','metaln15','metalc15',
            'metaln16','metalc16','metaln17','metalc17','metaln18','metalc18','metaln19','metalc19','metaln20','metalc20',
            'costcn','costnn','costn',
            'costn1','costc1','costn2','costc2','costn3','costc3','costn4','costc4','costn5','costc5',
            'costn6','costc6','costn7','costc7','costn8','costc8','costn9','costc9','costn10','costc10',
            'costn11','costc11','costn12','costc12','costn13','costc13','costn14','costc14','costn15','costc15',
            'costn16','costc16','costn17','costc17','costn18','costc18','costn19','costc19','costn20','costc20'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'details': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'details'
            }),
            'gradegrp': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'gradegrp'
            }),
            'misc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'misc'
            }),
            'metaln': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln',
            }),
            'costn': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn',
            }),
            'metalnn': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metalnn',
            }),
            'costnn': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costnn',
            }),
            'costcn': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costcn',
            }),
            'metalc': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc',
            }),
            'metalcn': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalcn',
            }),
            'costc': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc',
            }),
            'metaln1': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln1',
            }),
            'metalc1': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc1',
            }),
            'metaln2': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln2',
            }),
            'metalc2': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc2',
            }),
            'metaln3': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln3',
            }),
            'metalc3': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc3',
            }),
            'metaln4': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln4',
            }),
            'metalc4': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc4',
            }),
            'metaln5': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln5',
            }),
            'metalc5': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc5',
            }),
            'metaln6': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln6',
            }),
            'metalc6': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc6',
            }),
            'metaln7': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln7',
            }),
            'metalc7': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc7',
            }),
            'metaln8': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln8',
            }),
            'metalc8': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc8',
            }),
            'metaln9': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln9',
            }),
            'metalc9': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc9',
            }),
            'metaln10': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln10',
            }),
            'metalc10': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc10',
            }),
            'metaln11': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln11',
            }),
            'metalc11': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc11',
            }),
            'metaln12': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln12',
            }),
            'metalc12': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc12',
            }),
            'metaln13': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln13',
            }),
            'metalc13': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc13',
            }),
            'metaln14': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln14',
            }),
            'metalc14': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc14',
            }),
            'metaln15': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln15',
            }),
            'metalc15': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc15',
            }),
            'metaln16': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln16',
            }),
            'metalc16': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc16',
            }),
            'metaln17': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln17',
            }),
            'metalc17': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc17',
            }),
            'metaln18': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln18',
            }),
            'metalc18': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc18',
            }),
            'metaln19': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln19',
            }),
            'metalc19': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc19',
            }),
            'metaln20': forms.Select(attrs={
                'class': 'form-control col', 'id': 'metaln20',
            }),
            'metalc20': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalc20',
            }),
            'costn1': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn1',
            }),
            'costc1': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc1',
            }),
            'costn2': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn2',
            }),
            'costc2': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc2',
            }),
            'costn3': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn3',
            }),
            'costc3': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc3',
            }),
            'costn4': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn4',
            }),
            'costc4': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc4',
            }),
            'costn5': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn5',
            }),
            'costc5': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc5',
            }),
            'costn6': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn6',
            }),
            'costc6': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc6',
            }),
            'costn7': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn7',
            }),
            'costc7': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc7',
            }),
            'costn8': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn8',
            }),
            'costc8': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc8',
            }),
            'costn9': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn9',
            }),
            'costc9': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc9',
            }),
            'costn10': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn10',
            }),
            'costc10': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc10',
            }),
            'costn11': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn11',
            }),
            'costc11': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc11',
            }),
            'costn12': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn12',
            }),
            'costc12': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc12',
            }),
            'costn13': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn13',
            }),
            'costc13': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc13',
            }),
            'costn14': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn14',
            }),
            'costc14': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc14',
            }),
            'costn15': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn15',
            }),
            'costc15': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc15',
            }),
            'costn16': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn16',
            }),
            'costc16': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc16',
            }),
            'costn17': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn17',
            }),
            'costc17': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc17',
            }),
            'costn18': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn18',
            }),
            'costc18': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc18',
            }),
            'costn19': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn19',
            }),
            'costc19': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc19',
            }),
            'costn20': forms.Select(attrs={
                'class': 'form-control col', 'id': 'costn20',
            }),
            'costc20': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'costc20',
            }),



            
            'typeo': forms.Select(attrs={
                'class': 'form-control col', 'id': 'typeo'
            }),
            'recovery': forms.TextInput(attrs={
                'class': 'form-control col', 'id': 'recovery'
            }),

        } 





class QualityForm(forms.ModelForm):
     class Meta:
        model = Quality
        
        fields = [
            'supplier','yard','grade','metalw' ,'metalwc' ,'metalw1' ,'metalw2' ,'metalw3' ,'metalw4' ,'metalw5' ,'metalw6' ,'metalw7' ,'metalw8' ,'metalw9' ,'metalw10' ,'metalw11' ,'metalw12' ,'metalw13' ,'metalw14' ,'metalw15' ,'metalw16' ,'metalw17' ,'metalw18' ,'metalw19' ,'metalw20','duty'
        ]

        widget = {
            'supplier': forms.Select(attrs={
                'class': 'form-control col', 'id': 'supplier'
            }),
            'yard': forms.Select(attrs={
                'class': 'dropdown', 'id': 'yard'
            }),
            'grade': forms.Select(attrs={
                'class': 'form-select col', 'id': 'grade'
            }),
            'metalw': forms.NumberInput(attrs={
               'class':'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'id': 'metalw'
            }),
            'metalwc': forms.NumberInput(attrs={
                'class':'form-control col', 'id': 'metalw1'
            }),
            'metalw1': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw1',
            }),
            'metalw2': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw2',
            }),

            'metalw3': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw3',
            }),
            'metalw4': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw4',
            }),

            'metalw5': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw5',
            }),

            'metalw6': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw6',
            }),

            'metalw7': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw7',
            }),

            'metalw8': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw8',
            }),

            'metalw9': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw9',
            }),

            'metalw10': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw10',
            }),

            'metalw11': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw11',
            }),

            'metalw12': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw12',
            }),

            'metalw13': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw13',
            }),

            'metalw14': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw14',
            }),

            'metalw15': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw15',
            }),

            'metalw16': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw16',
            }),

            'metalw17': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw17',
            }),

            'metalw18': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw18',
            }),

            'metalw19': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw19',
            }),

            'metalw20': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'metalw20',
            }),
            'duty': forms.NumberInput(attrs={
                'class': 'form-control col', 'id': 'duty',
            }),
        }