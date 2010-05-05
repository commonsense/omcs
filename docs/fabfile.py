from fabric.api import run, sudo, env, local
print "WARNING: The fabric script has not been updated to use git."

config = env
config.hosts = ['anemone.media.mit.edu']
config.build_output = '/srv/csc/documentation/_build/html/'
config.target = '/srv/csc/cscweb/static/docs/'

virtualenv = 'source /srv/csc/bin/activate'

def test():
    local('make html')
    
def run_list(lst):
    run(' && '.join(lst))

def local_bzr_commit():
    env.warn_only = True
    local('bzr commit', capture=False)
    env.warn_only = False

def bzr_update(project, develop=True):
    lst = ['cd "/srv/csc/%s"' % project,
           'bzr up']
    if develop: lst += [virtualenv, 'python setup.py develop']
    run_list(lst)

def update_deps():
    for project in ['csc-utils', 'conceptnet', 'divisi']:
        bzr_update(project, develop=True)

def update_src():
    bzr_update('documentation', develop=False)

def build():
    run_list([virtualenv,
              'cd /srv/csc/documentation',
              'make html'])

def clean():
    run_list([virtualenv,
              'cd /srv/csc/documentation',
              'make clean'])
def publish():
    local_bzr_commit()
    update_deps()
    update_src()
    build()
    run('rsync -rlpgoDvP --delete "%s" "%s"' % (env.build_output, env.target))

def update(): publish()
