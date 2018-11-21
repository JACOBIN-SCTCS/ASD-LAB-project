from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from .models import Todo
from django.views.generic.edit import UpdateView
from .forms import AddTodoForm



# Create your views here.

def index(request):
    all_todos=Todo.objects.all().order_by('priority')
    return render(request,'main/index.html',{'todos':all_todos})


def addtodopage(request):
    if request.method=='POST':
        form=AddTodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.save()

            return redirect('main:index')
    else:
        form=AddTodoForm()
    return render(request,'main/addform.html',{'form':form})

    

class TodoUpdateView(UpdateView):
    model=Todo
   

    form_class=AddTodoForm

    template_name_suffix='_update_form'

    def get_success_url(self):
        return reverse('main:index')

def deletetodo(request,id):
    todo=Todo.objects.get(todo_id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('main:index'))

    