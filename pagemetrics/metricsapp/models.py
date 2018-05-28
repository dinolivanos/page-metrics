from django.db import models

SUCCESS = 'SUCCESS'
PENDING = 'PENDING'
STATES = frozenset({SUCCESS, PENDING})
TASK_STATE_CHOICES = sorted(zip(STATES, STATES))


class Metric(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Page(models.Model):
    url = models.URLField()
    description = models.TextField()

    reports = models.ManyToManyField(Metric, through='Report')

    def __str__(self):
        return self.url


class Report(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    status_date = models.DateTimeField()
    status = models.CharField(
        'state',
        max_length=50, default=PENDING,
        choices=TASK_STATE_CHOICES,
    )

    report = models.URLField()

    class Meta:
        ordering = ["-status_date"]

    def __str__(self):
        return '{}, {}, {}'.format(self.status_date, self.metric, self.page)
