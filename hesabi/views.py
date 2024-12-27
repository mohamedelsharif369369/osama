from django.shortcuts import render,redirect,get_object_or_404
from .models import Hesabi
from .forms import HesabiForm , HesabiUpdateForm

# Create your views here.

def hesabi(request):
    if request.method == 'POST':
        hesabi_form = HesabiForm(request.POST)
        if hesabi_form.is_valid():
            hesabi_form.save()
            return redirect('/hesabi')
    else:
        hesabi_form = HesabiForm()
    hesabi = Hesabi.objects.all()
    return render(request,'hesabi/hesabi.html',{
        'hesabi':hesabi,'hesabi_form':hesabi_form
        })


def edit_hesabi(request, pk):
    obj = get_object_or_404(Hesabi, pk=pk)
    if request.method == 'POST':
        edit_form = HesabiUpdateForm(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/hesabi')
    else:
        edit_form = HesabiUpdateForm(instance=obj)
    return render(request,'hesabi/edit_hesabi.html',{'edit_form':edit_form})



def delete_hesabi(request, pk):
    obj = get_object_or_404(Hesabi, pk=pk)
    if request.method == 'POST':
        edit_form = HesabiUpdateForm(request.POST,instance=obj)
        obj.delete()
        return redirect('/hesabi')
    return render(request,'hesabi/delete_hesabi.html',{'object':obj})