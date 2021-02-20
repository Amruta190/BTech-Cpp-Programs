def word_freq(lt):
    dic={}
    for i in lt:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    return dic
ipfile=open("text1.txt",'r')
l_5B9=ipfile.read().split("\n")
lt=[]
for i in l_5B9:
    for j in i.split():
        lt.append(j.lower())
freq_count=word_freq(lt)
n=max(list(freq_count.values()))
print("Most frequently occuring words and its frequency")
for key,value in freq_count.items():
    if value==n:
        print(key,value)