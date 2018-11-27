from os import system
from time import sleep

def clear():
    system('clear')

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if(y == 0):
        print ("Division by ZERO!!!")
        return None
        
    return x / y

def mathFunc(func, x, y):
    print("Answer is: " + str(func(int(x),int(y))))

cnt = True
while cnt:
    clear()
    oper = input("""
    What is your operation
        Addition
        Subtraction
        Multiplication
        Division
        Quit
        
        PLEASE ENTER (+, -, *, /, q): """)

    clear()
    if(oper == '+'):
        print ("Addition")
        mathFunc(add, input("First Number: "), input("Second Number: "))
    elif(oper == '-'):
        print ("Subtraction")
        mathFunc(sub, input("First Number: "), input("Second Number: "))
    elif(oper == '*'):
        print ("Multiplication")
        mathFunc(mul, input("First Number: "), input("Second Number: "))
    elif(oper == '/'):
        print ("Division")
        mathFunc(div, input("First Number: "), input("Second Number: "))
    elif(oper == 'q'):
        print ("Quiting...")
        cnt = False
    else:
        print ("""
        Invalid Input
        Please choose between +, -, *, /
        or enter q to Quit
        Try Again""")
        
    sleep(2)
    clear()