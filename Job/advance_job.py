def calculat(num_1, oparator, num_2):
    if oparator == "plus" :
        print(num_1 + num_2)

    elif oparator == 'minus':
        print(num_1 - num_2)

    elif oparator == 'multilply':
        print(num_1 * num_2)
    elif oparator == 'divided':
        print(num_1 / num_2)
    else:
        print("something else, please check and try again")

calculat(10,'divided',1)
