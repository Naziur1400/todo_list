from django.shortcuts import render,redirect

from .models import Todo

def index(request):

	todos = Todo.objects.all()
	context = {
		'todos': todos
	}
	return render(request,'todos/index.html', context)


def detail(request, todo_id):
	detail = Todo.objects.get(id=todo_id)
	detail = {
		'detail': detail
	}
	return render(request, 'todos/details.html',detail)

def add(request):
	
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']

		todo = Todo(title=title, text=text)
		todo.save()

		return redirect('/')

	else:
		return render(request, 'todos/add.html')
