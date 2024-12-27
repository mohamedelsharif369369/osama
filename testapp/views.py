from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView , CreateView , DeleteView
from .forms import ImageUserForm ,ImageUpdateForm
from .models import Test , ImageUser
# Create your views here.

class TestListView(ListView):
    model = Test
    template_name='test/test.html'
    context_object_name = 'test'

class TestDetailView(DetailView):
    model = Test
    template_name='test/test_detail.html'
    context_object_name = 'test'

class TestUpdateView(UpdateView):
    model = Test
    fields = ['name','age','job']
    template_name='test/test_update.html'
    success_url = reverse_lazy('test')


class TestCreateView(CreateView):
    model = Test
    fields = ['name','age','job']
    template_name = "test/test_create.html"
    success_url = reverse_lazy('test')


class TestDeleteView(DeleteView):
    model = Test
    template_name = "test/test_delete.html"
    success_url = reverse_lazy('test')

def img(request):
    if request.method == 'POST':
        img_form = ImageUserForm(request.POST,request.FILES)
        if img_form.is_valid():
            img_form.save()
            return redirect('/testapp/img')
    else:
        img_form = ImageUserForm()
    img = ImageUser.objects.all()
    return render(request,'test/img.html',{'img':img,'img_form':img_form})

def edit_img(request, pk):
    obj = get_object_or_404(ImageUser, pk=pk)
    if request.method == 'POST':
        edit_form = ImageUpdateForm(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/testapp/img')
    else:
        edit_form = ImageUpdateForm(instance=obj)
    return render(request,'test/edit_img.html',{'edit_form':edit_form})


def delete_img(request, pk):
    obj = get_object_or_404(ImageUser, pk=pk)
    if request.method == 'POST':
        edit_form = ImageUpdateForm(request.POST,instance=obj)
        obj.delete()
        return redirect('/testapp/img')
    return render(request,'test/delete_img.html',{'object':obj})

