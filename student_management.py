import json

filename="list.json"


def save_student():
    pass

def load():
    try:
        with open (filename,"r") as file:
            return json.load(file)
    except:
        return {"lists:[]"}



def save_tasks(student):
    try:
        with open(filename,"w")as file:
            json.dump(student,file)
    except:
        return {"failed"}

def Add(student):
    name=input("Enter name of student: ").lower().strip()
    id=int(input("Enter student id: ").strip())

    if name and id:
        student["lists"].append({"Name":name,"Id":id})
        save_tasks(student)
        print("Added Success.")
        
    else:
        print("Not Filled every entry.")


def Read(student):
    list=student["lists"]
    if len(list)==0:
        print("NO entry")
        return
    for idx,name in enumerate(list):
        print(f"{idx+1}. {name['Name']} {name['Id']}")

def Update(student):
    name =input("Enter student to update id: ").lower().strip()
    id=int(input("Enter to update: ").strip())
    list=student["lists"]
    for _,stud in enumerate(list):
        if(stud['Name']==name):
            stud['Id']=id
            save_tasks(student)
            print("Updated")
            return
    print("Student not found")


def  Delete(student):
    name=input("Enter student name: ").lower().strip()
    list=student["lists"]
    for i,data in enumerate(list):
        if data['Name']==name:
            del list[i]
            save_tasks(student)
            print("Deletd Success")
            return
    print("Not Found")


def main():
    while True:
        student=load()
        print("1. ADD")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        b=False
        choice=int(input("Enter Number: ").strip())
        match choice:
            case 1:
                Add(student)
            case 2:
                Read(student)
            case 3:
                Update(student)

            case 4:
                Delete(student)
            case 5:
                b=True
            case _:
                print("Invalid")
        if b:
            break




main()

