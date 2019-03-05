from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html' ,
		{'all_items': all_todo_items})
def addTodo(request):
	#create todoitem and save item
	new_item = TodoItem(content =request.POST['content'])
	new_item.save()
	#redirect to '/todo/'
	return HttpResponseRedirect('/todo/') 
def deleteTodo(request, todo_id):
	#Retrive todo item by its Id
	item_to_delete = TodoItem.objects.get(id = todo_id)
	item_to_delete.delete()
	#redirect to '/todo/'
	return HttpResponseRedirect('/todo/') 