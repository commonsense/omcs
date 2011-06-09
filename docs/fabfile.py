from __future__ import with_statement
from fabric.api import *
from fabric.contrib.project import rsync_project

env.hosts = ['anemone.media.mit.edu']

def test():
    build_docs()

def deploy():
    push()
    update_server()

def update_server():
    # later, make this assemble things on the server side
    # this requires understanding how it's set up, though
    rsync_project(local_dir='_build/html/', remote_dir='/srv/csc/cscweb/static/docs/')

def push():
    build_docs()
    local('git pull origin master', capture=False)
    local('git push origin master', capture=False)

def git_dance():
    local('git commit -av', capture=False)
    local('git pull origin master', capture=False)
    local('git push origin master', capture=False)

def build_docs():
    local('make html', capture=False)

