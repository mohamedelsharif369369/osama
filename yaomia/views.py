from django.shortcuts import render,redirect,get_object_or_404
from .models import Yaomia
from .forms import YaomiaForm , YaomiaUpdateForm

# Create your views here.

def yaomia(request):
    if request.method == 'POST':
        yaomia_form = YaomiaForm(request.POST)
        if yaomia_form.is_valid():
            yaomia_form.save()
            return redirect('/yaomia')
    else:
        yaomia_form = YaomiaForm()
    yaomia = Yaomia.objects.all()
    return render(request,'yaomia/yaomia.html',{
        'yaomia':yaomia,'yaomia_form':yaomia_form
        })



def edit_yaomia(request, pk):
    obj = get_object_or_404(Yaomia, pk=pk)
    if request.method == 'POST':
        edit_form = YaomiaUpdateForm(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/yaomia')
    else:
        edit_form = YaomiaUpdateForm(instance=obj)
    return render(request,'yaomia/edit_yaomia.html',{'edit_form':edit_form})



def delete_yaomia(request, pk):
    obj = get_object_or_404(Yaomia, pk=pk)
    if request.method == 'POST':
        edit_form = YaomiaUpdateForm(request.POST,instance=obj)
        obj.delete()
        return redirect('/yaomia')
    return render(request,'yaomia/delete_yaomia.html',{'object':obj})
