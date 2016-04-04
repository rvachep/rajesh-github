from fabric.api import local

def test():
  local("./manage.py")

def commit():
  local("git add . && git commit -m 'testing fabric with git local'")

def push():
  local("git push origin master")

