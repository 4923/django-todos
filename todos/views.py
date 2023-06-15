from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo 
from .forms import TodoForm

# Create your views here.
# @login_required 
def index(request):
    completed = request.GET.get('completed') or False
    todos = Todo.objects.filter(completed=completed)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user # 작성자 정보 
            todo.save()
    else:
        form = TodoForm()
    
    context = {
        'form': form,
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todos:index')