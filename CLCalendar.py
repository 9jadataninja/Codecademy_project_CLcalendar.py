# Codecademy_project_CLcalendar.py
"""
This is a command line calendar that allows the user to choose ot view the calendar, add an event to the calendar, update an existing event, delete an existing event
"""
from time import sleep, strftime
USER_NAME = "Opetunde"
calendar = {}
def welcome():
  print "Hello " + USER_NAME
  print "Calendar opening..."
  sleep(1)
  print "Today's date is " + strftime("%A %B %d, %Y")
  print " The time is " + strftime("%H:%M:%S")
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Press A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar 
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful!"
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "You entered an invalid date."
        try_again = raw_input("try again/ Y for Yes, N for No: ")
        try_again =try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event 
        print 'Event was succesfully added!'
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print 'The event was successfully deleted'
          else:
            print "an incorrect event was specified"
    elif user_choice == "X":
      start = True
    else:
      print 'An invalid command was entered'
      exit
start_calendar()   
