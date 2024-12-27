
from django.shortcuts import render,redirect,get_object_or_404
from .models import Servie
from .forms import ServieForm , ServieUpdateForm

# Create your views here.
   
def servies(request):
    if request.method == 'POST':
        servie_form = ServieForm(request.POST)
        if servie_form.is_valid():
            servie_form.save()
            return redirect('/servies')
    else:
        servie_form = ServieForm()
    servie = Servie.objects.all()
    return render(request,'servies/servies.html',{
        'servie':servie,'servie_form':servie_form
        })

def edit_servies(request, pk):
    obj = get_object_or_404(Servie, pk=pk)
    if request.method == 'POST':
        edit_form = ServieUpdateForm(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/servies')
    else:
        edit_form = ServieUpdateForm(instance=obj)
    return render(request,'servies/edit_servies.html',{'edit_form':edit_form})



def delete_servies(request, pk):
    obj = get_object_or_404(Servie, pk=pk)
    if request.method == 'POST':
        edit_form = ServieUpdateForm(request.POST,instance=obj)
        obj.delete()
        return redirect('/servies')
    return render(request,'servies/delete_servies.html',{'object':obj})