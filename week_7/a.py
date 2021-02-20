vowels="aeiouAEIOU"
s_5B9=input("Enter a string : ")
count=sum([1 for i in s_5B9 if i in vowels])
print("The no.of vowels in "+s_5B9+" is "+str(count))