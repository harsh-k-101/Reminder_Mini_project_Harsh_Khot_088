
#import subprocess

import event_reminder
import assignment_reminder
import sedentary_reminder

from plyer import notification




choice = 0 

print("Hi this is reminder notification program enter your choice:")
print("For adding a specific reminder press: 1 \nFor setting a sedentry reminder press: 2 \nAssignment Reminder press: 3\nTo exit the app press z \n")


while choice != 'z' :
    choice = input(" Enter your choice: ")

    if choice == '1' :
        event_reminder.event_notification()
        event_reminder.snooze()
        #popen('python event_reminder.py ')

    elif choice == '2' :
        sedentary_reminder.run_sedentary()
        #popen('python sedentary_reminder.py')
       
    elif choice == '3' :
        assignment_reminder.run_assignment()
     
    elif choice == 'z':
        print("Exiting the app: ")

    else:
        print("Invalid option !! enter again:")

