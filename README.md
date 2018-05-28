# Install and setup
Rabbitmq message broker

```brew install rabbitmq```


The RabbitMQ server scripts are installed into /usr/local/sbin. This is not automatically added to your path, so you may wish to add PATH=$PATH:/usr/local/sbin to your .bash_profile or .profile. The server can then be started with rabbitmq-server.

All scripts run under your own user account. Sudo is not required.

```
cd /usr/local/sbin/
rabbitmqctl add_user pagemetrics metrics123
rabbitmqctl add_vhost pagemetrics_vhost
rabbitmqctl set_user_tags pagemetrics pagemetrics_tag
rabbitmqctl set_permissions -p pagemetrics_vhost pagemetrics ".*" ".*" ".*"
```

Create celery dB

```python manage.py migrate django_celery_results```

Create django admin

```bash
python manage.py createsuperuser
```

Start rabbitmq

```/usr/local/sbin/rabbitmq-server ```

Start celery


```
cd pagemetrics
celery -A pagemetrics worker -l info
```

# Testing

```
cd pagemetrics
./manage.py test
```

# Misc

To have launchd start rabbitmq now and restart at login:
  brew services start rabbitmq
Or, if you don't want/need a background service you can just run:
  rabbitmq-server


http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
https://tests4geeks.com/python-celery-rabbitmq-tutorial/
python -m test_celery.run_tasks


./manage.py test metricsapp.tests.ReportTestCase


python manage.py makemigrations metricsapp
python manage.py migrate


