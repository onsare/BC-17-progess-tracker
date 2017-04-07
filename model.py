db = {"username" : '', "password" : "", "tasks" : {}}

def username():
  
  return db["username"]

def password():
  return db["password"]

def get_tasks():
  return db['tasks']

def get_task(task):
  return task in get_tasks() 

def get_progress(task):
  if task in db['tasks']:
    return db['tasks'].task
  else:
    return 0

def insert_task(task):
  if task not in db['tasks']:
      db['tasks'][task] = 0
      return True
  else:
    return False

def insert_progress(task, progress):
  if task in db['tasks']:
    db['tasks'][task] = progress
    return True
  else:
    return False
