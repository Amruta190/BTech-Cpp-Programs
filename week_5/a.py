L1_5B9=[1,2,3,4,5]
L2_5B9=[11,12,13,14,15]
print(f"L1 = {L1_5B9}")
print(f"L2 = {L2_5B9}")
L3_5B9=L1_5B9+L2_5B9
print(f"Adding L1 and L2 gives L3 : {L3_5B9}")
L3_5B9.insert(3,7)
print(f"Inserting 7 at index 3 of L3 gives {L3_5B9}")
print(f"Slicing the list L3 from index 4 to 7 (both inclusive) gives : {L3_5B9[4:8]}")