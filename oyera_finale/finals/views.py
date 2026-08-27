from django.shortcuts import render,redirect
from .forms import PartForm
from .models import Part

# Create your views here.
def homePage(request):
    return render(request, 'finals/index.html')


# Part model
def addPart(request):
    if request.method == 'POST':
        data = request.POST
        form = PartForm(data)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = PartForm()
        context = {
            "part_form":form
        }
    return render (request,'finals/part_form.html',context)

def editPart(request, part_id):
    part = Part.objects.get(id = part_id)
    if request.method == 'POST':
        form = PartForm(request.POST,instance= part)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = PartForm(instance = part)
    context = {
            'title':'Apply changes',
            'part':part
        }
    return render(request, 'finals/part_form.html', context)

def partView(request):
    parts = Part.objects.all()
    context = {
        'parts': parts
    }
    return render(request, 'finals/view_part.html', context) 

def deletePart(request, part_id):
    parts = Part.objects.get(id = part_id)
    if request.method =='POST':
        parts.delete()
        return redirect('view_part')

    context ={
        'parts':parts
    }
    return render(request,'finals/confirm_delete.html', context)

def success(request):
    return render(request,'finals/success.html')


# the Job 





    
        