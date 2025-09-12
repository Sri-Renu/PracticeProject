# JavaScript Object Notation (JSON)

import json
FILENAME = "students.json"

def load_data(filename=FILENAME):
    with open(filename,"r") as f:
        return json.load(f)

# indent=4 → makes the file nicely formatted instead of one-line messy text (nice readable format with 4 spaces indentation)
def save_data(data,filename=FILENAME):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)
# json.dumps(obj) → returns JSON as a string
# json.dump(obj, file) → writes JSON to a file

def add_student(filename=FILENAME):
    try:
        student_id=int(input("Enter the ID: "))
        univ_roll=input("Enter the University Roll: ")
        name=input("Enter the Name: ")
        cgpa=float(input("Enter the CGPA: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
        return

    new_student={"id":student_id, "univ_roll": univ_roll,"name":name,"cgpa":cgpa}

    data=load_data(filename)
    data.append(new_student)
    save_data(data,filename)
    print(f"Student added successfully with ID: {new_student['id']}")

def delete_student(filename=FILENAME):
    try:
        student_id=int(input("Enter the ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
        return

    data=load_data(filename)
    new_data=[s for s in data if s["id"]!=student_id]
    if len(new_data)==len(data):
        print(f"Student with ID {student_id} not found.")
    else:
        save_data(new_data,filename)
        print(f"Student with ID {student_id} deleted successfully.")

def update_student(filename=FILENAME):
    try:
        student_id=int(input("enter the id to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
        return

    data=load_data(filename)
    for s in data:
        if s["id"] == student_id:
            print(f"Current record: {s}")
            print("Leave input blank if you don't want to change that field.")
            
            new_univ_roll=input(f"Enter new University Roll (current: {s['univ_roll']}): ") or s['univ_roll']
            new_name = input(f"Enter new Name (current: {s['name']}): ") or s['name']
            try:
                new_cgpa_input=input(f"Enter new CGPA (current: {s['cgpa']}): ")
                new_cgpa=float(new_cgpa_input) if new_cgpa_input else s['cgpa']
            except ValueError:
                print("Invalid CGPA. keeping old value.")
                new_cgpa= s['cgpa']

            s['univ_roll']= new_univ_roll
            s['name']=new_name
            s['cgpa']=new_cgpa

            save_data(data,filename)
            print(f"Student with id {student_id} updated successfully.")
            return

    print(f"Student with ID {student_id} not found.")    
def view_all_students():
    students = load_data()
    print("\n--- ALL STUDENTS ---")
    for s in students:
        print(f"ID: {s['id']} | Roll: {s['univ_roll']} | Name: {s['name']} | CGPA: {s['cgpa']}")

def search_by_id():
    students=load_data()
    try:
        student_id=int(input("Enter the ID to search: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
        return
    for s in students:
        if s['id']==student_id:
            print(f"\nFound: {s}")
            return
    print("Student not found.")


def menu():
    while True:
        print("\n========= STUDENT DATA PROCESSOR =========\n")
        print("1. view all students")
        print("2. search students by ID")
        print("3. add a student")
        print("4. delete a student")
        print("5. update student")
        print("6. exit")

        choice=input("enter choice: ")

        if choice == "1":
            view_all_students()
        elif choice == "2":
            search_by_id()
        elif choice == "3":
            add_student()
        elif choice=="4":
            delete_student() 
        elif choice =="5":
            update_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    menu()

#(Logical issue, not code enforced) → If you add a student with an already existing ID, the program will still add it. You’ll get duplicate IDs in JSON.