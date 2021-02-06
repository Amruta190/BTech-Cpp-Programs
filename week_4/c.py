a=input("Enter a string: ")
b=input("ENter the substring to check : ")
if b in a:
    print(f"Yes, {b} is present in {a}")
else:
    print(f"No!!, {b} is not present in {a}")