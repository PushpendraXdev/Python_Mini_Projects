import json

filename="to_do_list.json"
def load_tasks():
    try:
        with open(filename,"r")as file:
         return json.load(file)
    except:
        return {"tasks:[]"}



def save_tasks(tasks):
    try:
        with open(filename,"w")as file:
            json.dump(tasks,file)
    except:
        return {"failed"}


def view_tasks(tasks):
    take_list=tasks["tasks"]
    if len(take_list)==0:
        print("NO tasks")
    else:
        print("your to do list:")
        for idx,task in enumerate(take_list):
            status="[completed]" if task["complete"] else "[pending]"
            print(f"{idx+1}. {task['description']} | {status}")



def create_tasks(tasks):
    description=input("Enetr the task description: ").strip()
    if description:
        tasks["tasks"].append({"description":description,"complete":False})
        save_tasks(tasks)
    else:
        print("Description cannot empty.")

def mark(tasks):
    view_tasks(tasks)
    try:
        task_number=int(input("enter the task number to mark: ").strip())
        if 1<=task_number<=len(tasks["tasks"]):
            tasks['tasks'][task_number-1]["complete"]=True
            save_tasks(tasks)
            print("Task is Marked")
        else:
            print("Inval545id")
    except:
        print("Invalid")

def main():
    tasks=load_tasks()
    while True:
        print("\nTO_DO List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice=input("Enter task number: ")
        if choice=="1":
            view_tasks(tasks)
        elif choice=="2":
            create_tasks(tasks)
        elif choice=="3":
            mark(tasks)
        elif choice=="4":
            print("GoodBye")
            break
        else:
            print("Invalid")
main()

