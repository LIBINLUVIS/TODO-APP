from django.shortcuts import render,redirect
from . models import *
from .forms import *
# Create your views here.


def index(request):
    tasks = task.objects.all()  
    form = TaskForm()
    if request.method=='POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

        
    temp = {'tasks':tasks,'form':form}

    return render(request,'list.html',temp)


def updateTask(request, pk):
	var = task.objects.get(id=pk)

	form = TaskForm(instance=var)


	if request.method == 'POST':
		form = TaskForm(request.POST, instance=var)
		if form.is_valid():
			form.save()
			return redirect('/')

	temp = {'form':form}

	return render(request, 'update_task.html', temp)

def deleteTask(request, pk):
	item = task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'delete.html',context)
