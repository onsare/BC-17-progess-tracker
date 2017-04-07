import logic

import ui

ui.print_menu()

user_input = logic.user_input("Please Enter your selection")
if user_input == "1":
  pass
  # insert task
elif user_input == "2":
  pass
  course = logic.user_input("Please enter your task")
  # query dictionary
else:
  ui.print_message("Good-bye Thanks for Using Progress Tracker")