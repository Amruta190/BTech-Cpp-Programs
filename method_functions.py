L1=[10,20,30,'a',['b',22,64],'queue',50]
print(f"Length of L1 is {len(L1)}")
L1.append('xyz')
print(f"L1 after appending 'xyz' : {L1}")
L2=["apple","banana","watermelon"]
L1.extend(L2)
print(f"L1 after extend(L2) : {L1}")
L1.remove('queue')
print(f"L1 after removing 'queue' : {L1}")
print(f"Last element in L1 : {L1.pop()}")
del L1[3]
print(f"L1 after deleting element in index 3 : {L1}")
L1.clear()
print(f"L1 after using L1.clear() : {L1}")