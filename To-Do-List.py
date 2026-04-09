tasks = []
action = 0

def get_valid_action(prompt):
    while True:
        try : 
            action = int(input(prompt + "\n"))

            if action <1 or action >4:
                print ("Please choose your action from the number 1-4.\n")

            else :
                return action
            
        except ValueError:
            print("Please enter a valid number.\n")


def get_valid_task(prompt):
    while True:
        try : 
            i = int(input(prompt + "\n"))

            if (i-1) > len(tasks) or (i -1) < 0:
                print ("Please select a number for an existing task. \n")

            else :
                return i
            
        except ValueError:
            print("Please enter a valid number.\n")

def main ():
    while True:
        print ("1. Add task \n2. View tasks \n3. Mark task as done \n4. Quit")
        action = get_valid_action("Please enter the number of the corresponding action that you would like to perform")

        if action == 1:
            add_task()
        elif action == 2:
            view_task()
        elif action == 3 :
            mark_task_as_done()
        else :
            break
        

def add_task () :
    name = input("Please enter the task name")
    done = False
    tasks.append({"name" : name, "done" : done})

def view_task():
    for i, task in enumerate(tasks):
        print(f"{i +1}. {task["name"]} : {task["done"]} ")
    
def mark_task_as_done():
    i = get_valid_task("Please enter the task number of the task you completed") -1
    tasks[i]["done"] = True


