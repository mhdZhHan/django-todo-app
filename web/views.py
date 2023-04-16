from django.shortcuts import render, redirect
from django.http import JsonResponse
# from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from task.models import Task


@login_required(login_url='/users/login/')
def index(request):
    tasks = Task.objects.filter(is_completed=False, is_deleted=False, owner=request.user)
    completed_tasks = Task.objects.filter(is_completed=True, is_deleted=False, owner=request.user)

    if request.method == 'POST':
        if request.POST['task_title'] != '':
            title = request.POST['task_title']
            todo = Task(title=title, owner=request.user)
            todo.save()

    context = {
        'title': 'Django Todo | Add Todo',
        'tasks': tasks,
        'compleated_tasks': completed_tasks
    }

    return render(request, 'web/index.html', context)


@login_required(login_url='/users/login/')
def update_task(request, pk):
    if Task.objects.filter(pk=pk).exists():
        if request.method == 'POST':
            task = Task.objects.get(pk=pk)

            if request.POST.get('new_task_title') != '':
                task.title = request.POST.get('new_task_title')
                task.save()

                # Return success response
                response_data = {'status': 'success', 'data': 'Task updated successfully'}
            else:
                response_data = {'status': 'success', 'data': 'Add a value'}
                return JsonResponse(response_data)
        else:
            response_data = {'status': 'error', 'data': 'Task not updated'}

        return JsonResponse(response_data)
    else:
        return redirect('/')


@login_required(login_url='/users/login/')
def complete_task(request, pk):
    # task = get_object_or_404(Task, id=pk)
    if Task.objects.filter(pk=pk).exists():
        task = Task.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        return redirect('/')
        # return JsonResponse({'success': True})
    else:
        return redirect('/')


@login_required(login_url='/users/login/')
def undo_task(request, pk):
    # task = get_object_or_404(Task, id=pk)
    if Task.objects.filter(pk=pk).exists():
        task = Task.objects.get(pk=pk)
        task.is_completed = False
        task.save()
        return redirect('/')
        # return JsonResponse({'success': True})
    else:
        return redirect('/')


@login_required(login_url='/users/login/')
def delete_task(request, pk):
    # task = get_object_or_404(Task, id=pk)
    if Task.objects.filter(pk=pk).exists():
        task = Task.objects.get(pk=pk)
        task.is_deleted = True
        task.save()
        return redirect('/')
        # return JsonResponse({'success': True})
    else:
        return redirect('/')
