my_dictionary = {"my_name" : "takowa",
                "my_car" : 'bmw',
                 "my_home" : "dabirgonj"
                 }
print(my_dictionary)

del my_dictionary["my_car"]  #use del keyword for delet dictionary's key and value
print(my_dictionary)

x = my_dictionary.pop("my_home")   # use pop for delet last item and return last item value
print(my_dictionary) 

print(x)   # last item value 

my_dictionary["bank_account"] = "nai"    # add item in dictionary

print("bank_account" in my_dictionary)
print(my_dictionary)
print(my_dictionary["bank_account"])


print(my_dictionary.keys())   # print all keys
print(my_dictionary.values()) #print all values

print(my_dictionary.clear())
 