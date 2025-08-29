def ripon_mia(call):
    def wrapar(): 
        print("ha ha")
        call()
        print("etai bastob")
    return wrapar

@ripon_mia
def name():
    print("takowa ullah")
name()

