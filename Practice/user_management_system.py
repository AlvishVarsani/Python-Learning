import json

print("User Management System")
print("1. Add User")
print("2. View Users")
print("3. Update User")
print("4. Delete User")
# print("5. Exit")
# print("6. Continue")
choice = int(input("Enter your choice: "))

match choice:
   case 1:
     try: 
      with open("users.json", "r") as file:
         name = input("Please add your name")
         user=json.load(file)
     except (FileNotFoundError,json.JSONDecodeError):
        user=[]
     new_user = {
            "name": name
        }
     user.append(new_user)
     with open("users.json", "w") as file:
        json.dump(user, file, indent=4)

     print("User added successfully!")
          
   case 2:
       with open ("users.json","r") as file:
          fileread=json.load(file)
          print(fileread)
   case 3: 
       with open("users.json", "r") as file:
            content = json.load(file)
       currentUser = input("Enter what name to be updated: ")
       updatedUser = input("Enter what correct name: ")

       for x in content:  
        if x["name"] == currentUser:
           x["name"] = updatedUser
           with open("users.json", "w") as file:
               json.dump(content, file, indent=4)
           print("User updated successfully!")
       else:
           print("User not found.")
   case 4: 
       deleteUser = input("Enter user to be deleted: ")
       with open("users.json", "r") as file:
           content = json.load(file)
       for x in content:    
        if x["name"] == deleteUser:
           content.remove(x)
           with open("users.json", "w") as file:
               json.dump(content, file, indent=4)
           print("User deleted successfully!")
           break
       else:
           print("User not found.")
