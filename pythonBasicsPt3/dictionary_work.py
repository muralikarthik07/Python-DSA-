stu = {}

while True:
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E. Delete a student")
    print("F. Exit")

    choice = input("enter your choice: ").upper()

    if choice == "A":
        name = input("enter the name: ")
        marks = int(input("enter the marks: "))
        stu[name] = marks
        print("student added successfully")

    elif choice == "B":
        stu_name = input("enter the name: ")
        if stu_name in stu:
            new_marks = int(input("re-enter marks: "))
            stu[stu_name] = new_marks
            print("Sucessfully updated marks")
    
    elif choice == "C":
        name = input("enter name: ")
        if name in stu:
            print(f"{name} has {stu[name]}")
        else:
            print("student not found")

    elif choice == "D":
        for name, marks in stu.items():
            print(f"{name}: {marks}")

    elif choice == "E":
        del_name = input("enter the name to delete: ")
        if del_name in stu:
            del stu[del_name]
            print("sucessfully deleted")
        else:
            print("student not found")



    elif choice == "F":
        print("Exiting the program")
        break