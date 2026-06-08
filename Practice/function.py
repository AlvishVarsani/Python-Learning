import random

x="Alvish"
def print_name():
    print(x)
print_name()

print(random.randrange(1,10))

users={"name":"Alvish","age":20,"country":"India"}
print(users["name"])
print(users["age"])
users["name"]="Alvish Kumar"
print(users["name"])

#print if "free" is presnt
txt="This is best free time"
if "free" in txt:
    print("True")
else : print("False")

a = "Hello, Horld!"
print(a.replace("H", "J"))


def my_funtion():
    return "True"

if my_funtion() in "True":
    print("Yes")
else:    print("No")


x=10;
"Ten" if x==10 else "eleven" if x==11 else "Twelve";