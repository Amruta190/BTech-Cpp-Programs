def multireturn(x):
    return (x,x*2)
n=int(input('Enter a number : '))
a,b=multireturn(n)
print(f"{a} and {b}")