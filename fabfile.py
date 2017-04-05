#-*- coding: utf-8 -*-
import os
from fabric.api import local, run, env, cd, lcd, settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env.hosts = ['user@149.154.70.39']
env.key_filename = '/home/fork/.ssh/id_rsa'

username = 'user'
urlname = 'site.ru'
projectname = 'project'

def migration():
    with cd('/var/www/%s/data/www/%s/release/' % (username, urlname)):
        run('docker exec %s_site_1 bash -c "cd /var/www; python3 manage.py makemigrations main; python3 manage.py migrate main"' % projectname)


def stop():
    with settings(warn_only=True):
        with cd('/var/www/%s/data/www/%s/release/' % (username, urlname)):
            run('docker-compose -f docker-compose.prod.yml -p %s stop' % projectname)
            run('docker-compose -f docker-compose.prod.yml -p %s rm -f' % projectname)


def update():
    with cd('/var/www/%s/data/www/%s' % (username, urlname)):
        run('rm -rf ./release')
        run('git clone ./ ./release')


def build():
    with cd('/var/www/%s/data/www/%s/release/' % (username, projectname)):
        run('docker-compose -f docker-compose.prod.yml -p %s build site' % projectname)


def start():
    with cd('/var/www/%s/data/www/%s/release/' % (urlname, projectname)):
        run('docker-compose -f docker-compose.prod.yml -p %s up -d' % projectname)


def deploy(migrate=False):
    stop()
    update()
    build()
    start()

    if migrate:
        migration()


def restart():
    stop()
    start()






