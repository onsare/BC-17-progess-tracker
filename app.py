import logic

import ui
import model

ui.print_menu()

user_input = logic.user_input("Please Enter your selection")
if user_input == "1":
  task = logic.user_input("Please enter your task: ")
  model.insert_task(task)
  #makes program pause 
  user_input = logic.user_input("Press any key to continue")
elif user_input == "2":
  pass
  course = logic.user_input("Please enter your task to be queried")
  # query dictionary
else:
  ui.print_message("Good-bye Thanks for Using Progress Tracker")