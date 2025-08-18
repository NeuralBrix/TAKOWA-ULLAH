my_set = set()
# set unike ,
# unorder
# mutable



student_list = ['takowa', 'mahim', 'rakib', 'seam', 'imtiaz','takowa' ]
print(student_list)   # print dublicate item

student_set = set(student_list)
print(student_set)

# basic oparation

my_set.add("pagla")  #add item
print(my_set)

student_set.remove("takowa")  #remove item
print(student_set)  

student_set.discard("rakib")  #remove item
print(student_set)

student_set.pop()   # as set is unorder so reomve a random item
print(student_set)

student_set.clear()
print(student_set)

# set olparation

set_a = {1,2,3,4}
set_b = {5,3,4,8}   # uniun 

print(set_a.union(set_b))  
print(set_a | set_b)        # pipe character means union  ,,, | = union

print(set_a.intersection(set_b))  
print(set_a & set_b) # intersection = &
