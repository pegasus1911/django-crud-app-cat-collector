from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Cat, Toy
from .forms import FeedingForm
from django.views.generic import ListView,DetailView

# FUNCTION BASED VIEWS
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cat_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })
  
def cat_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  feeding_form=FeedingForm()
  print('cat: ', cat)
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form':feeding_form,'toys':toys})

# CLASS BASED VIEWS
class CatCreate(CreateView):
  model = Cat
  fields = ['name','breed','description','age']

  # success_url = "/cats/"\

class CatUpdate(UpdateView):
  model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

def add_feeding(request,cat_id):
  form=FeedingForm(request.POST)
  if form.is_valid():
    new_feeding=form.save(commit=False)
    new_feeding.cat_id=cat_id
    new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)

class ToyCreate(CreateView):
  model=Toy
  fields='__all__'
class ToyList(ListView):
  model=Toy
class ToyDetail(DeleteView):
  model=Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'  