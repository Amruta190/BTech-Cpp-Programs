for i in range(20,51):
    count_5B9=0
    for j in range(1,i+1):
        if i%j==0:
            count_5B9+=1
    if count_5B9==2:
            print(i)