def print_menu():
    '''
    display menu 
    '''
    print_message("Welcome to progress Tracker")
    print_message("PLease insert 1 for to insert a task")
    print_message("Please insert 2 for to query ")
    print_message("Please insert 3 to view all tasks and progress")
    print_message("Press any other key to quit")


def print_message(message):
    '''
    :param message: 
    :return: none
    '''
    print(message)

def print_progress(task, progress, many = False):
  if many == False:
    print("_"*20 )
    print("Task" + " "*8 + 'Progress' )
  print(str(task) + " "*10 + str(progress)+ "%")