
def helloWorld(int):
    i = 0
    while i < int:
        print('Hellow World')
        i+=1


def getUserInput():
    return int(input("Enter a number: "))
    
helloWorld(getUserInput())
