import array
arr_5B9=array.array('i',[1,2,3,6,7,5])
print(arr_5B9)
arr1_5B9=array.array('i',[20,21,22,23,24,25])
arr2_5B9=array.array('i',arr1_5B9+arr_5B9)
print(f"After appending: {arr2_5B9}")
arr_5B9.insert(1,50)
print(f"After inserting 50 at index 1: {arr_5B9}")
arr_5B9.reverse()
print(f"After reversing: {arr_5B9}")