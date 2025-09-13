def avarage(my_list):
    total = 0
    for num in my_list:
        total += num        
    return total / len(my_list)

my_list = [1,2,3,4,5]
x = avarage(my_list)
print(x)