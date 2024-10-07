from app.sample_tasks import slow_fib
from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def run_task(request):
    if request.method == 'POST':
        value = request.POST.get("value")
        task = slow_fib.delay(int(value))

        return JsonResponse({"task_id": task.id}, status=202)



@csrf_exempt
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)