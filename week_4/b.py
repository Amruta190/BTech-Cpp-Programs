def check(a,b):
    if(sorted(a)==sorted(b)):
        print(f"{a} and {b} are anagrams")
    else:
        print(f"{a} and {b} are not anagrams")
a_5B9=input("Enter 1st string : ")
b_5B9=input("Enter 2nd string : ")
check(a_5B9,b_5B9)