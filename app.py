import logic

import ui
import model
while(True):
  ui.print_menu()

  user_input = logic.user_input("Please Enter your selection")
  if user_input == "1":
    task = logic.user_input("Please enter your task: ")
    progress = logic.user_input("Please enter your task progress")

    model.insert_task(task)
    model.insert_progress(task, progress)
    #makes program pause
    user_input = logic.user_input("Press any key to continue")
  elif user_input == "2":
    pass
    course = logic.user_input("Please enter your task to be queried")
    # query dictionary
    model.print_progress(course,model.db['tasks'][course] )
  else:
    ui.print_message("Good-bye Thanks for Using Progress Tracker")
    break