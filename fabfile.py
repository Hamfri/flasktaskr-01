from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
    with settings(warn_only=True):
        result = local("nosetests -v", capture=True)
    if result.failed and not confirm("Tests failed. Continue?"):
        abort("Aborted at user request.")

def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add -A && git commit -am'{}'".format(message))

def push():
    local("git branch")
    branch = raw_input("Which branch do you want to push to?")
    local("git push origin {}".format(branch))

def prepare():
    test()
    commit()
    push()

def pull():
    local("git pull origin master")

def heroku():
    local("git push heroku master")

def heroku_test():
    local("heroku run nosetests -v")
    local("heroku ps")
    local("heroku open")

def deploy():
    #pull()
    #test()
    heroku()
    heroku_test()

def rollback():
    local("heroku rollback")
    
    
def create_app():
    local("heroku apps:create flasktasks")
    local("git push heroku master")
    local("heroku addons:create heroku-postgresql:hobby-dev")
    local("heroku ps")
    local("heroku open")
    local("heroku logs")

def create():
    create_app()
