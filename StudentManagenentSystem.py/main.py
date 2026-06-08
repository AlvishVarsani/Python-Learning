print("1. Add Student")
print("2. View Students")
print("3. Search Students")
print("4. Delete Student")
print("5. Exit")

student=[]

while True:
    user_input = input("Enter your choice: ")
    match user_input:
        case "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            student.append({"name": name, "age": age})
            print(f"Student {name} added successfully!")
        case "2":
            print("Student List:", student)
        case "3":
            search_name = input("Enter student name to search: ")
            found_students = [s for s in student if s["name"] == search_name]

            if found_students:
                print("Student found:", found_students)
            else:
                print("Student not found.")        
        case "4":
            delete_name = input("Enter student name to delete: ")
            student = [s for s in student if s["name"] != delete_name]
            print(f"Student {delete_name} deleted successfully!")
        case "5":
            print("Exiting the program.")
            break
           