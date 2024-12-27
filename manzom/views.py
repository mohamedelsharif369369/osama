from django.shortcuts import render,redirect,get_object_or_404
from .models import Manzom
from .forms import ManzomForm , ManzomUpdateForm


# Create your views here.

def manzom(request):
    if request.method == 'POST':
        manzom_form = ManzomForm(request.POST,request.FILES)
        if manzom_form.is_valid():
            manzom_form.save()
            return redirect('/manzom')
    else:
        manzom_form = ManzomForm()
    manzom = Manzom.objects.all()
    return render(request,'manzom/manzom.html',{'manzom':manzom,'manzom_form':manzom_form})




def edit_manzom(request, pk):
    obj = get_object_or_404(Manzom, pk=pk)
    if request.method == 'POST':
        edit_form = ManzomUpdateForm(request.POST,request.FILES,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/manzom')
    else:
        edit_form = ManzomUpdateForm(instance=obj)
    return render(request,'manzom/edit_manzom.html',{'edit_form':edit_form})



def delete_manzom(request, pk):
    obj = get_object_or_404(Manzom, pk=pk)
    if request.method == 'POST':
        edit_form = ManzomUpdateForm(request.POST,request.FILES,instance=obj)
        obj.delete()
        return redirect('/manzom')
    return render(request,'manzom/delete_manzom.html',{'object':obj})