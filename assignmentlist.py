#, by the end of each day, you’ll have a clear overview of what you completed and what still needs attention

# Simple Daily Task Organizer

cheaklist = ["python assignment","read books","exercise","reply to emails"]
completed_tasks =[]
incompleted_tasks =[]

for task in cheaklist:
    if input(f"did you complete this '{task}'? (y/n):").lower()=='y':
        completed_tasks.append(task)
    else:
        incompleted_tasks.append(task)

print("\nCompleted Task:",completed_tasks)
print("Incompleted Tasks:",incompleted_tasks)

# input(..)- is a built-in function in Python that pauses the program and waits for the user to type something.
# f - f-string - allows you to insert variables directly into a string
#.lower() - is a string method that converts all letters in a string to lowercase
