# Install
Rabbitmq message broker

```brew install rabbitmq```


The RabbitMQ server scripts are installed into /usr/local/sbin. This is not automatically added to your path, so you may wish to add PATH=$PATH:/usr/local/sbin to your .bash_profile or .profile. The server can then be started with rabbitmq-server.

All scripts run under your own user account. Sudo is not required.

```
rabbitmqctl add_user pagemetrics metrics123
rabbitmqctl add_vhost pagemetrics_vhost
rabbitmqctl set_user_tags pagemetrics pagemetrics_tag
rabbitmqctl set_permissions -p pagemetrics_vhost pagemetrics ".*" ".*" ".*"
```

Start rabbitmq

```/usr/local/sbin/rabbitmq-server ```

Start celery

```celery -A test_celery worker --loglevel=info```




# Misc

To have launchd start rabbitmq now and restart at login:
  brew services start rabbitmq
Or, if you don't want/need a background service you can just run:
  rabbitmq-server


https://tests4geeks.com/python-celery-rabbitmq-tutorial/
python -m test_celery.run_tasks