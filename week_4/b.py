def check(a,b):
    if(sorted(a)==sorted(b)):
        print(f"{a} and {b} are anagrams")
    else:
        print(f"{a} and {b} are not anagrams")
a=input("Enter 1st string : ")
b=input("Enter 2nd string : ")
check(a,b)