x = 20
print(x)
def area():
    x = 0
    print(x)
    def sub_area():
        global x 
        x = 50     
    sub_area()
area()

print(f"global x : {x}")


#---------------------------------------------------------------------------------------------------------------------------------------

#non local


def outer():
    x = 5
    def inner():
        nonlocal x   # for access to op 
        x += 50
        print(x)
    inner()
outer()

#----------------------------------------------------------------------------------------------------------------

# function return

def add(a,b):
    x = a + b
    return x

result = add(2,3)
print(result)

