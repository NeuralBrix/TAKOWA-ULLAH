def first_funct(funct):
    funct()
    return "its my first funct"

def secound_funct():
    print("its secount funct")


my_var = first_funct(funct=secound_funct)
print(my_var)