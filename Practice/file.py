# # file=open("file.txt","w")
# # file.write("Hello World")
# # file.close()

# file=open("file.txt","r")
# # print(file.read())
# file.close()

# with open("file.txt","r") as file:
#     print(file.readline())
#     print(file.readline())

# #Read all lines
# with open("file.txt","r") as file:
#     lines=file.readlines()
# print(lines)            

with open("file.txt","w") as file:
    file.write("Alvish Varsani\n")
    file.write("Ahmedabad\n")

with open("file.txt","r") as file:
    print(file.read())

with open("file.txt","a") as file:
    file.write("India")

with open("file.txt","r") as file:
    x=0
    for line in file:
        x+=1
    print(x)
        
file.close()

with open("user.json","r") as file:
    print(file.read())
file.close()

with open ("file.txt","r") as file:
    line1=0
    word=0
    char=0
    for line in file:
        line1+=1
        word+=len(line.split())
        char+=len(line.strip())
    print(f"Lines: {line1}")
    print(f"Words: {word}")
    print(f"Characters: {char}")
