names = ['Rahim', "karim", "Sabina", "Ayesha", "hasan", "Monir", "shirin"]
markes_list = [85, 72, 80, 90, 76, 88, 69]

my_dictionary = dict(zip(names,markes_list))
print(my_dictionary)

dict_values = my_dictionary.values()
x = sum(dict_values)
y = dict_values.__len__()
print("the avarage number is:",(x/y))

