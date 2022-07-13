from multiprocessing import context
import os
import re
from urllib import request
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django import forms as formsm
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


error = ""
error2 = ""

from users.models import User
from .models import (  
    Quality,
    Supplier,
    Yard,
    cost,
    grade, metal,
)
from .forms import (
    CostUpdateform,
    GradeUpdateform,
    # MakeAndModelForm,
    MetalUpdateform,
    QualityForm,
    SupplierForm,
    YardForm,
    SupplierUpdateForm,
    YardUpdateForm, CostForm, GradeForm, MetalForm,
    # demoForm
)



def files():
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    json_serializer.serialize(metal.objects.all())
    data = json_serializer.getvalue()

    data = list(metal.objects.values_list("id","shortform"))
    a_file = open("./data_metal.json", "w")
    json.dump(data, a_file)
    a_file.close()
    with open("./data_metal.json", "r") as source, open("./static/assets/js/data_metal.json", "w") as dest:
        dest.write(source.read()) 
    # with open("./static/assets/js/data_metal.json","w") as out:
    #     json_serializer.serialize(metal.objects.all(), stream=out)
    # data = list(cost.objects.values_list("id","rate"))
    # a_file = open("./data.json", "w")
    # json.dump(data, a_file)
    # a_file.close()
    # with open("data.json", "r") as source, open("./static/assets/js/data.json", "w") as dest:
    #     dest.write(source.read()) 

    data = list(cost.objects.values_list("name","rate"))
    a_file = open("./data.json", "w")
    json.dump(data, a_file)
    a_file.close()
    with open("./data.json", "r") as source, open("./static/assets/js/data.json", "w") as dest:
        dest.write(source.read())  


    data = list(Yard.objects.values_list("supplier","name","id"))
    a_file = open("./yard.json","w")
    json.dump(data,a_file)
    a_file.close()
    with open("./yard.json","r") as source, open("./static/assets/js/yard.json","w") as dest:
        dest.write(source.read())

    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    json_serializer.serialize(grade.objects.all())
    data = json_serializer.getvalue()

    with open("./static/assets/js/data_grade.json","w") as out:
        json_serializer.serialize(grade.objects.all(), stream=out)    


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        global error
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            contact = forms.cleaned_data['contact']
            mob_no = forms.cleaned_data['mob_no']
            email = forms.cleaned_data['email']
            ename = forms.cleaned_data['ename']
            econtact = forms.cleaned_data['econtact']
            emob_no = forms.cleaned_data['emob_no']
            eemail = forms.cleaned_data['eemail']


            Supplier.objects.create(name=name, address=address, contact=contact,mob_no=mob_no,email=email,ename=ename,econtact=econtact,
                emob_no=emob_no, eemail=eemail
            )
            files()
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'




def update_supplier(request, pk):
	queryset = Supplier.objects.get(id=pk)
	form = SupplierUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = SupplierUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
            
			return redirect('supplier-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_supplier.html', context)  


def delete_supplier(request, pk):
	queryset = Supplier.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('supplier-list')
	return render(request, 'store/delete_items.html')   






def create_yard(request, pk):
    supplier = Supplier.objects.get(id=pk)
    yards = Yard.objects.filter(supplier=supplier)
    form = YardForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            yard = form.save(commit=False)
            yard.supplier = supplier
            yard.save()
            return redirect("detail-yard", pk=yard.id)
        else:
            return render(request, "partials/yard_form.html", context={
                "form": form
            })
    files()
    context = {
        "form": form,
        "supplier": supplier,
        "yards": yards
    }

    return render(request, "store/create_yard.html", context)


def update_yard(request, pk):
    yard = Yard.objects.get(id=pk)
    form = YardForm(request.POST or None, instance=yard)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-yard", pk=yard.id)
    files()
    context = {
        "form": form,
        "yard": yard
    }

    return render(request, "partials/yard_form.html", context)


def delete_yard(request, pk):
    yard = get_object_or_404(Yard, id=pk)

    if request.method == "POST":
        yard.delete()
        return HttpResponse("")
    files()
    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_yard(request, pk):
    yard = get_object_or_404(Yard, id=pk)
    context = {
        "yard": yard
    }
    return render(request, "partials/yard_detail.html", context)


def create_yard_form(request):
    form = YardForm()
    context = {
        "form": form
    }
    return render(request, "partials/yard_form.html", context)




class CostListView(ListView):
    model = cost
    template_name = 'store/cost_list.html'
    context_object_name = 'cost'




def create_cost(request):
    forms = CostForm()
    if request.method == 'POST':
        forms = CostForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            shortform = forms.cleaned_data['shortform']
            rate = forms.cleaned_data['rate']
            misc = forms.cleaned_data['misc']
            cost.objects.create(
                name=name, shortform=shortform, rate=rate, misc=misc
            )
            files()
            return redirect('cost-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_cost.html', context)    



def update_cost(request, pk):
	queryset = cost.objects.get(id=pk)
	form = CostUpdateform(instance=queryset)
	if request.method == 'POST':
		form = CostUpdateform(request.POST, instance=queryset)

		if form.is_valid():
			form.save()
			return redirect('cost-list')
    
	context = {
		'form':form
	}
	return render(request, 'store/create_cost.html', context)    


def delete_cost(request, pk):
	queryset = cost.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('cost-list')
	return render(request, 'store/delete_items.html')    


def create_metal(request):
    forms = MetalForm()
    if request.method == 'POST':
        forms = MetalForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            shortform = forms.cleaned_data['shortform']
            misc = forms.cleaned_data['misc']
            metal.objects.create(
                name=name, shortform=shortform, misc=misc
            )
            files()
            return redirect('metal-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_metal.html', context)  

def update_metal(request, pk):
	queryset = metal.objects.get(id=pk)
	form = MetalUpdateform(instance=queryset)
	if request.method == 'POST':
		form = MetalUpdateform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()

			return redirect('metal-list')    

	context = {
		'form':form
	}
	return render(request, 'store/create_metal.html', context)    
files()

def delete_metal(request, pk):
	queryset = metal.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('metal-list')
	return render(request, 'store/delete_items.html')      

files()
class MetalListView(ListView):
    model = metal
    template_name = 'store/metal_list.html'
    context_object_name = 'metal'       

files()


model1 = ""

def create_grade(request):
    forms = GradeForm(use_required_attribute=False)
    # form = metal_grade()
    metaldict = []
    global model1
    if request.method == 'POST':
        forms = GradeForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            details = forms.cleaned_data['details']
            gradegrp = forms.cleaned_data['gradegrp']
            misc = forms.cleaned_data['misc']
            metaln = forms.cleaned_data['metaln']
            metalnn = forms.cleaned_data['metalnn']
            metalcn = forms.cleaned_data['metalcn']
            costc = forms.cleaned_data['costc']
            metalc = forms.cleaned_data['metalc']

            metaln1 = forms.cleaned_data['metaln1']
            metalc1 = forms.cleaned_data['metalc1']

            metaln2 = forms.cleaned_data['metaln2']
            metalc2 = forms.cleaned_data['metalc2']
            metaln3 = forms.cleaned_data['metaln3']
            metalc3 = forms.cleaned_data['metalc3']
            metaln4 = forms.cleaned_data['metaln4']
            metalc4 = forms.cleaned_data['metalc4']
            metaln5 = forms.cleaned_data['metaln5']
            metalc5 = forms.cleaned_data['metalc5']
            metaln6 = forms.cleaned_data['metaln6']
            metalc6 = forms.cleaned_data['metalc6']
            metaln7 = forms.cleaned_data['metaln7']
            metalc7 = forms.cleaned_data['metalc7']
            metaln8 = forms.cleaned_data['metaln8']
            metalc8 = forms.cleaned_data['metalc8']
            metaln9 = forms.cleaned_data['metaln9']
            metalc9 = forms.cleaned_data['metalc9']
            metaln10 = forms.cleaned_data['metaln10']
            metalc10 = forms.cleaned_data['metalc10']
            metaln11 = forms.cleaned_data['metaln11']
            metalc11 = forms.cleaned_data['metalc11']
            metaln12 = forms.cleaned_data['metaln12']
            metalc12 = forms.cleaned_data['metalc12']
            metaln13 = forms.cleaned_data['metaln13']
            metalc13 = forms.cleaned_data['metalc13']
            metaln14 = forms.cleaned_data['metaln14']
            metalc14 = forms.cleaned_data['metalc14']
            metaln15 = forms.cleaned_data['metaln15']
            metalc15 = forms.cleaned_data['metalc15']
            metaln16 = forms.cleaned_data['metaln16']
            metalc16 = forms.cleaned_data['metalc16']
            metaln17 = forms.cleaned_data['metaln17']
            metalc17 = forms.cleaned_data['metalc17']
            metaln18 = forms.cleaned_data['metaln18']
            metalc18 = forms.cleaned_data['metalc18']
            metaln19 = forms.cleaned_data['metaln19']
            metalc19 = forms.cleaned_data['metalc19']
            metaln20 = forms.cleaned_data['metaln20']
            metalc20 = forms.cleaned_data['metalc20']
            costn = forms.cleaned_data['costn']
            costnn = forms.cleaned_data['costnn']
            costcn = forms.cleaned_data['costcn']

            costn1 = forms.cleaned_data['costn1']
            costc1 = forms.cleaned_data['costc1']

            costn2 = forms.cleaned_data['costn2']
            costc2 = forms.cleaned_data['costc2']
            costn3 = forms.cleaned_data['costn3']
            costc3 = forms.cleaned_data['costc3']
            costn4 = forms.cleaned_data['costn4']
            costc4 = forms.cleaned_data['costc4']
            costn5 = forms.cleaned_data['costn5']
            costc5 = forms.cleaned_data['costc5']
            costn6 = forms.cleaned_data['costn6']
            costc6 = forms.cleaned_data['costc6']
            costn7 = forms.cleaned_data['costn7']
            costc7 = forms.cleaned_data['costc7']
            costn8 = forms.cleaned_data['costn8']
            costc8 = forms.cleaned_data['costc8']
            costn9 = forms.cleaned_data['costn9']
            costc9 = forms.cleaned_data['costc9']
            costn10 = forms.cleaned_data['costn10']
            costc10 = forms.cleaned_data['costc10']
            costn11 = forms.cleaned_data['costn11']
            costc11 = forms.cleaned_data['costc11']
            costn12 = forms.cleaned_data['costn12']
            costc12 = forms.cleaned_data['costc12']
            costn13 = forms.cleaned_data['costn13']
            costc13 = forms.cleaned_data['costc13']
            costn14 = forms.cleaned_data['costn14']
            costc14 = forms.cleaned_data['costc14']
            costn15 = forms.cleaned_data['costn15']
            costc15 = forms.cleaned_data['costc15']
            costn16 = forms.cleaned_data['costn16']
            costc16 = forms.cleaned_data['costc16']
            costn17 = forms.cleaned_data['costn17']
            costc17 = forms.cleaned_data['costc17']
            costn18 = forms.cleaned_data['costn18']
            costc18 = forms.cleaned_data['costc18']
            costn19 = forms.cleaned_data['costn19']
            costc19 = forms.cleaned_data['costc19']
            costn20 = forms.cleaned_data['costn20']
            costc20 = forms.cleaned_data['costc20']

            typeo = forms.cleaned_data['typeo']
            recovery = forms.cleaned_data['recovery']

            grade.objects.create(
                name=name, details=details, gradegrp=gradegrp, misc=misc,typeo=typeo, recovery=recovery,metaln=metaln,
                metalnn=metalnn,metalcn=metalcn, metalc=metalc, metaln1=metaln1, metalc1=metalc1,  metaln2=metaln2, metalc2=metalc2,
                metaln3=metaln3, metalc3=metalc3,  metaln4=metaln4, metalc4=metalc4,  metaln5=metaln5, metalc5=metalc5,  metaln6=metaln6, metalc6=metalc6, 
                metaln7=metaln7, metalc7=metalc7,  metaln8=metaln8, metalc8=metalc8,  metaln9=metaln9, metalc9=metalc9,  metaln10=metaln10, metalc10=metalc10,
                metaln11=metaln11, metalc11=metalc11, metaln12=metaln12, metalc12=metalc12, metaln13=metaln13, metalc13=metalc13, metaln14=metaln14, metalc14=metalc14, metaln15=metaln15, metalc15=metalc15,
                metaln16=metaln16, metalc16=metalc16, metaln17=metaln17, metalc17=metalc17,metaln18=metaln18, metalc18=metalc18,metaln19=metaln19, metalc19=metalc19,
                metaln20=metaln20, metalc20=metalc20,costn=costn,
                costnn=costnn,costcn=costcn, costc=costc, costn1=costn1, costc1=costc1,  costn2=costn2, costc2=costc2,
                costn3=costn3, costc3=costc3,  costn4=costn4, costc4=costc4,  costn5=costn5, costc5=costc5,  costn6=costn6, costc6=costc6, 
                costn7=costn7, costc7=costc7,  costn8=costn8, costc8=costc8,  costn9=costn9, costc9=costc9,  costn10=costn10, costc10=costc10,
                costn11=costn11, costc11=costc11, costn12=costn12, costc12=costc12, costn13=costn13, costc13=costc13, costn14=costn14, costc14=costc14, costn15=costn15, costc15=costc15,
                costn16=costn16, costc16=costc16, costn17=costn17, costc17=costc17,costn18=costn18, costc18=costc18,costn19=costn19, costc19=costc19,
                costn20=costn20, costc20=costc20
            )
            files()
            return redirect('grade-list')
        else:
            print(forms.errors.as_json())               
    context = {
        'form': forms,
        'cost': model1,
    }
    # if request.htmx == 'POST':
    #     return render(request, 'store/grade/book_form.html', context)       

    return render(request, 'store/create_grade.html', context) 

# def jsondata(request):



def show_grade(request):
    gradeobj = grade.objects.all()
    files()
    context = {'grade':gradeobj}
    return render(request, './tp.html',context)

    
#     return JsonResponse(data,safe = False)





def update_grade(request,pk):
    obj = get_object_or_404(grade,id=pk)
    print(obj)
    form= GradeForm(request.POST or None, instance=obj)

    context = {'form': form}

    if form.is_valid():
        # print(form)
        obj = form.save(commit=False)
        obj.save()
        files()
        return redirect('grade-list')
    else:
        print(form.errors.as_json())    

    context = {'form': form}
        
    return render(request, 'store/create_grade.html',context)


# data = serializers.serialize("json", grade.objects.all())
# print(data)
# a_file = open("./data_grade.json", "w")
# json.dump(data, a_file)
# a_file.close()



def delete_grade(request, pk):
	queryset = grade.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('grade-list')
	return render(request, 'store/delete_items.html')      


class GradeListView(ListView):
    model = grade
    template_name = 'store/grade_list.html'
    context_object_name = 'grade'     



def Quality_View(request):
    forms = QualityForm()
    gradeobj = grade.objects.all()
    if request.method == 'POST':
        forms = QualityForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            yard = forms.cleaned_data['yard']
            grade1 = forms.cleaned_data['grade']
            metalw = forms.cleaned_data['metalw']
            metalw1 = forms.cleaned_data['metalw1']
            metalw2 = forms.cleaned_data['metalw2']
            metalw3 = forms.cleaned_data['metalw3']
            metalw4 = forms.cleaned_data['metalw4']
            metalw5 = forms.cleaned_data['metalw5']
            metalw6 = forms.cleaned_data['metalw6']
            metalw7 = forms.cleaned_data['metalw7']
            metalw8 = forms.cleaned_data['metalw8']
            metalw9 = forms.cleaned_data['metalw9']
            metalw10 = forms.cleaned_data['metalw10']
            metalw11 = forms.cleaned_data['metalw11']
            metalw12 = forms.cleaned_data['metalw12']
            metalw13 = forms.cleaned_data['metalw13']
            metalw14 = forms.cleaned_data['metalw14']
            metalw15 = forms.cleaned_data['metalw15']
            metalw16 = forms.cleaned_data['metalw16']
            metalw17 = forms.cleaned_data['metalw17']
            metalw18 = forms.cleaned_data['metalw18']
            metalw19 = forms.cleaned_data['metalw19']
            metalw20 = forms.cleaned_data['metalw20']


            Quality.objects.create(
                supplier = supplier, yard=yard, grade=grade1,
                metalw=metalw, metalw1=metalw1, metalw2=metalw2,
                 metalw3=metalw3, metalw4=metalw4, metalw5=metalw5, metalw6=metalw6, 
                 metalw7=metalw7, metalw8=metalw8, metalw9=metalw9, metalw10=metalw10,
                 metalw11=metalw11, metalw12=metalw12, metalw13=metalw13,  metalw14=metalw14, metalw15=metalw15,
                 metalw16=metalw16, metalw17=metalw17, metalw18=metalw18, metalw19=metalw19,
                 metalw20=metalw20
            )
            files()
            return redirect('supplier-list')
        else:
            print(forms.errors.as_json())    
    context = {
        'form': forms,
    }
    return render(request, 'store/quality.html', context)


def create_quality(request):
    qualitys = Quality.objects.all()
    form = QualityForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            quality = form.save(commit=False)
            quality.save()
            return redirect("detail-quality", pk=quality.id)
        else:
            return render(request, "partials/quality_form.html", context={
                "form": form
            })
    files()
    context = {
        "form": form,
        "qualitys": qualitys,
        "suppliers": Supplier
    }

    return render(request, "store/create_quality.html", context)


def update_quality(request, pk):
    quality = Quality.objects.get(id=pk)
    form = QualityForm(request.POST or None, instance=quality)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-quality", pk=quality.id)

    context = {
        "form": form,
        "quality": quality
    }

    return render(request, "partials/quality_form.html", context)


def delete_quality(request, pk):
    quality = get_object_or_404(Quality, id=pk)

    if request.method == "POST":
        quality.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_quality(request, pk):
    quality = get_object_or_404(Quality, id=pk)
    context = {
        "quality": quality
    }
    return render(request, "partials/quality_detail.html", context)


def create_quality_form(request):
    form = QualityForm()
    context = {
        "form": form
    }
    return render(request, "partials/quality_form.html", context)
 


files()



# with open("./data_grade.json", "r") as source, open("./static/assets/js/data_grade.json", "w") as dest:
#     dest.write(source.read())     






















