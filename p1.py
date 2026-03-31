def add_student():
    try:
        name = input("enter the name:")
        marks = int(input("enter the marks:"))

        if marks < 0 or marks > 100:
            raise ValueError("marks can't be negative or more then 100")

        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "E"

        with open("sample.txt","a") as f:
            f.write(f"{name},{marks},{grade}\n")

        print("Student added succesfully")

    except ValueError as e:
        print(e)

def view_student():
    try:
        with open("sample.txt","r") as f:
            print("Name Marks Grade")
            print("-------------------")
            for i in f:
                data = i.strip().split(",")
                print(data[0],"  ",data[1],"  ",data[2])
    except FileNotFoundError:
        print("No student data found")

while True:
    print("\n1.Add student")
    print("2.View student")
    print("3.Exit")

    choice = input("enter the choice:")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        print("Exiting.....")
        break
    else:
        print("Invalid choice, try again")

