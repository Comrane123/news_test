from celery.schedules import crontab

from .celery import app
from post.models import Post


@app.task
def clear_votes():
    post = Post.objects.all()
    post.update(number_of_votes=0)
    post.save()


app.conf.beat_schedule = {
    "run-every-single-day": {
        "task": "news_test.tasks.clear_votes",
        "schedule": crontab(),
    },
}
