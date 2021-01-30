s1=input("Enter 1st string : ")
s2=input("Enter 2nd string : ")
common=set(s2).intersection(set(s1))
print(f"Letters present in both the strings are : {common}")