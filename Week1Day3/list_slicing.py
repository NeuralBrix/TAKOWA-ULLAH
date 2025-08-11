list_1 = [4,5,2,54,67,4,2,4,6,8]

# the general syntax for list slicing is: list[start:end:step]

print(list_1[0:5:1])  # 0 to 5 index and step 1
print(list_1[0:10:2]) # 0 to 10 index and step 2

print(list_1[0::1])  # :: = end
print(list_1[9::-1])  #index 9 to end with negetive step

print(list_1[-1:-11:-1])   # use negetive indexing
print(list_1[-10::1])
print(list_1[::-1])