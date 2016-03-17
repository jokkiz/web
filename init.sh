sudo ln -sf /home/box/web/etc/test.conf /etc/nginx/sites-enabled/test.conf
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django_ask.py /etc/gunicorn.d/django_ask.py
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart

