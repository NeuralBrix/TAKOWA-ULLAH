def calculator():
    while True :
          try:
            calculat = input("inter your value: ")
            result = eval(calculat)
            print(result)
          except:
              print ("something else ")

calculator()
