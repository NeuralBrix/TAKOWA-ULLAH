def name(name):
    print(f"hello {name}")


name("takowa")


# 1st = positional perameter
def area(radias,length):
    print((3.14 * radias * radias) + length) 

area(10,2) #positional argument depended of position 
area(3,10) #positional argument depended of position 


# 2nd = keyword
def area(radias,length = 5):
    print((3.14 * radias * radias) + length)

area(10)
area(length=10, radias=3) #keyword argument not depended on position 


# var positional argument
def area(*arg):
    print(sum(arg))

area(2,3,2,4,5,4,3)

# 4th = args
def area(**arg):
    print(arg)


area(name = 3, nam = 2, man = 3)

#keyword only
def area(*,higth,lenth):
    print(higth+lenth)

area(higth=2,lenth=3)

# positional only

def area(higth,lenth,/):
    print(higth+lenth)
area(3,2)