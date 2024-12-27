from django.shortcuts import render,redirect
from .models import Manzoma,Hesabi,Masrof,Product,Servie,Yaomia
from .forms import ManzomaForm,HesabiForm,MasrofForm,ProductForm,ServieForm,YaomiaForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        manzoma_form = ManzomaForm(request.POST)
        hesabi_form = HesabiForm(request.POST)
        masrof_form = MasrofForm(request.POST)
        product_form = ProductForm(request.POST)
        servie_form = ServieForm(request.POST)
        yaomia_form = YaomiaForm(request.POST)
        if manzoma_form.is_valid():
            manzoma_form.save()
            return redirect('/')
        if hesabi_form.is_valid():
            hesabi_form.save()
            return redirect('/')
        if masrof_form.is_valid():
            masrof_form.save()
            return redirect('/')
        if product_form.is_valid():
            product_form.save()
            return redirect('/')
        if servie_form.is_valid():
            servie_form.save()
            return redirect('/')
        if yaomia_form.is_valid():
            yaomia_form.save()
            return redirect('/')
    else:
        manzoma_form = ManzomaForm()
        hesabi_form = HesabiForm()
        masrof_form = MasrofForm()
        product_form = ProductForm()
        servie_form = ServieForm()
        yaomia_form = YaomiaForm()
    manzoma = Manzoma.objects.all()
    hesabi = Hesabi.objects.all()
    masrof = Masrof.objects.all()
    product = Product.objects.all()
    servie = Servie.objects.all()
    yaomia = Yaomia.objects.all()
    return render(request,'home/home.html',{
        'manzoma':manzoma,'manzoma_form':manzoma_form,
        'hesabi':hesabi,'hesabi_form':hesabi_form,
        'masrof':masrof,'masrof_form':masrof_form,
        'product':product,'product_form':product_form,
        'servie':servie,'servie_form':servie_form,
        'yaomia':yaomia,'yaomia_form':yaomia_form,
        })
