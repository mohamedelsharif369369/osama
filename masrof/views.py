from django.shortcuts import render,redirect,get_object_or_404
from .models import Masrof
from .forms import MasrofForm , MasrofUpdateForm 

# Create your views here.




def masrof(request):
    if request.method == 'POST':
        masrof_form = MasrofForm(request.POST)
        if masrof_form.is_valid():
            masrof_form.save()
            return redirect('/masrof')
    else:
        masrof_form = MasrofForm()
    masrof = Masrof.objects.all()
    return render(request,'masrof/masrof.html',{
        'masrof':masrof,'masrof_form':masrof_form
        })

def edit_masrof(request, pk):
    obj = get_object_or_404(Masrof, pk=pk)
    if request.method == 'POST':
        edit_form = MasrofUpdateForm(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/masrof')
    else:
        edit_form = MasrofUpdateForm(instance=obj)
    return render(request,'masrof/edit_masrof.html',{'edit_form':edit_form})



def delete_masrof(request, pk):
    obj = get_object_or_404(Masrof, pk=pk)
    if request.method == 'POST':
        edit_form = MasrofUpdateForm(request.POST,instance=obj)
        obj.delete()
        return redirect('/masrof')
    return render(request,'masrof/delete_masrof.html',{'object':obj})