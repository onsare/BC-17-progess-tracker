import logic

import ui
import model
while(True):
  ui.print_menu()

  user_input = logic.user_input("Please Enter your selection: ")
  if user_input == "1":
    task = logic.user_input("Please enter your task: ")
    progress = logic.user_input("Please enter your task progress: ")

    model.insert_task(task)
    model.insert_progress(task, progress)
    #makes program pause
    logic.user_input("Press any key to continue")
  elif user_input == "2":
    course = logic.user_input("Please enter your task to be queried")
    # query dictionary
    if model.get_task(course):
        ui.print_progress(course, model.get_progress(course))
    else:
        ui.print_message("Sorry this task has not been added")
    logic.user_input("Press any key to continue")
  elif user_input == "3":
      many = False
      for task in model.get_tasks():
          ui.print_progress(task, model.get_progress(task), many)
          many = True
      if len(model.get_tasks()) == 0:
          ui.print_message("No task added yet ")
      #pause program for some time
      logic.user_input("Press any key to continue ")
  else:
    ui.print_message("Good-bye Thanks for Using Progress Tracker")
    break