vowels="aeiouAEIOU"
def vowelcount(x):
    c=sum([1 for i in x if i in vowels])
    return c
s_5B9=input("Enter some strings : ").split()
print(sorted(s_5B9,key=vowelcount))