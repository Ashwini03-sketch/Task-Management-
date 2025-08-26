#Task Management
from playsound import playsound

def task():
    task=[]
    print("\033[33m \n ------Welcome To The Task Management------ \033[0m")
    playsound(r"C:\Users\ASHWINI PARASHAR\Downloads\Python\Welcome To The Task Management .mp3")
    playsound(r"C:\Users\ASHWINI PARASHAR\Downloads\Python\Enter If You Want task management.mp3")

    total_task=int(input("\033[32m  Enter How Many task You want to Add : \033[0m").lower())
    for i in range(1,total_task+1):
        task_name=input(f"\033[32m Enter Task {i} : \033[0m")
        task.append(task_name)
    
    print(f"\033[31m \n Today's Task Are \n {task}  \033[0m")

    
    while True:
        operation = int(input("\033[32m \n Enter If You Want To --\n 1-Add \n 2-Update \n 3-Delete \n 4-view \n 5-Exit/Stop \033[0m"))
        if operation == 1:
            add=input("\033[32m \n Enter Task you Want To Add : \033[0m").lower()
            task.append(add)
            print(f"\033[31m Task {add} has been sucessfully added...\033[0m")
        
        
        elif operation == 2:
            update=input("\033[32m  \n Enter The Task Name You Want To Update : \033[0m").lower()
            if update in task:
                up=input("\033[32m  Enter New Task : \033[0m").lower()
                ind2=task.index(update)
                task[ind2]=up
                print(f"\033[34m  Updated Task {up} \033[0m")
            else:
                print("\033[31m  There Is No Such Task Available...\033[0m")
                
        elif operation==3:
            delete=input("\033[32m  \n Which Task You Want To Delete : \033[0m").lower()
            if delete in task:
                ind3 = task.index(delete)
                del task[ind3] 
                print(f"\033[34m  Task has been deleted \033[0m")
            else:
                print("\033[31m  There Is No Such Task Available... \033[0m")
                
        elif operation == 4:
                print(f"\033[34m  \n Total Task are : {task} \033[0m")
            
        elif operation == 5:
            print("\033[34m  Closing The Program....\033[0m")
            break
        
        else:
            print("\033[31m  \n Invalid Input :( \033[0m")
task()