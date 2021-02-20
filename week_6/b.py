from operator import itemgetter
import operator
def char_frequency(str):
    dic={}
    for n in str:
        if n in dic.keys():
            dic[n]+=1
        else:
            dic[n]=1
    return dic
a_5B9=char_frequency(input("Enter the string : "))
d=sorted(a_5B9.items(),key=operator.itemgetter(1),reverse=True)
for i in range(int(input("Enter n value to retrieve top n elements : "))):
    print(d[i])