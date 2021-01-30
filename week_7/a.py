vowels="aeiouAEIOU"
s=input("Enter a string : ")
count=sum([1 for i in s if i in vowels])
print("The no.of vowels in "+s+" is "+str(count))