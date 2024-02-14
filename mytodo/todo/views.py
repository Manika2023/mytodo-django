from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from todo.models import Todo
# Create your views here.
def todo_list(request):
     list=Todo.objects.all()
     if request.method=="POST":
          title=request.POST.get('title')
          desc=request.POST.get('desc')
          ins=Todo(title=title,description=desc)
          ins.save()
     data={
          'list':list
     }     
     return render(request,'index.html',data)

def delete_data(request,id):
     if request.method=="POST":
          obj=Todo.objects.get(pk=id)
          obj.delete()
          return HttpResponseRedirect('/')
     
def search(request):
     if request.method=="GET":
          s=request.GET.get('search_title')
          if s!=None:
               data=Todo.objects.filter(title__icontains=s)
          context={
           'data':data
            }          
          return render(request,'search.html',context)
     
