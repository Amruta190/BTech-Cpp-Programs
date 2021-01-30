arr=list(map(int,input("Enter space separated numbers : ").split()))
evenlist=[i for i in arr if i%2==0]
print(f"List of even numbers in given list is : {evenlist}")