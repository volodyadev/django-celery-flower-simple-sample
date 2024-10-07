import time

from celery import shared_task


@shared_task
def slow_fib(value):
    if value <= 0:
        return 0
    elif value == 1:
        return 1
    else:
        return slow_fib(value - 1) + slow_fib(value - 2)