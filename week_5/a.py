L1=[1,2,3,4,5]
L2=[11,12,13,14,15]
print(f"L1 = {L1}")
print(f"L2 = {L2}")
L3=L1+L2
print(f"Adding L1 and L2 gives L3 : {L3}")
L3.insert(3,7)
print(f"Inserting 7 at index 3 of L3 gives {L3}")
print(f"Slicing the list L3 from index 4 to 7 (both inclusive) gives : {L3[4:8]}")