# Install and setup
setup lighthouse which is a node package

```bash
cd lighthouse
npm instll
```

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

# Django Admin Site
user name: admin

password: adminadmin

# Testing

```
cd pagemetrics
./manage.py test
pytest metricsapp/metrics.py
```

