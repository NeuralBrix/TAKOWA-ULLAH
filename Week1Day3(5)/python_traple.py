my_tup = ()
# immuatable
# ordered
# dublicate support

tup_1 = (1,2,3)
tup_2 = (2,3,4)
#concatenate

print(tup_1 + tup_2)


this_tup = (1,2,3,4)
print(this_tup[1::2])
print(this_tup[1::])


print(1 in this_tup)
print(8 in this_tup)


x = 20,10,2 # packing
print(x)

x, y, z = (20,10,2)  # unpacking
print(y)
print(x)
print(z)