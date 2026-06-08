import sys

print("Alvish")
print(sys.version)
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")    