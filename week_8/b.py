dic={1:1,2:4,3:9,4:16,5:25}
n=int(input("Enter a key : "))
if n in list(dic.keys()):
    print(True)
else:
    print(False)