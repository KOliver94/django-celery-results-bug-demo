from celery import shared_task


@shared_task
def demo_task():
    return "Successful execution."
