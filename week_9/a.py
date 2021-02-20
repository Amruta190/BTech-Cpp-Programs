ipfile=open("text1.txt",'r')
l_5B9=ipfile.read().split("\n")
lt=[]
for i in l_5B9:
    for j in i.split():
        lt.append(j.lower())
lt.sort()
print(lt)
opfile=open("output.txt",'w')
for i in lt:
    opfile.write(str(i)+"\n")
ipfile.close()
opfile.close()