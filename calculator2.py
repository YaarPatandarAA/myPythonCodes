from os import system
from time import sleep

def clear():
    system('clear')

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
        try:
            print ( (lambda x,y: x + y) ( int(input("First Number: ")), int(input("Second Number: ")) ))
        except ValueError:
            print ("Please enter an Integer, Try Again!!")
    elif(oper == '-'):
        print ("Subtraction")
        try:
            print ( (lambda x,y: x - y) ( int(input("First Number: ")), int(input("Second Number: ")) ))
        except ValueError:
            print ("Please enter an Integer, Try Again!!")
    elif(oper == '*'):
        print ("Multiplication")
        try:
            print ( (lambda x,y: x * y) ( int(input("First Number: ")), int(input("Second Number: ")) ))
        except ValueError:
            print ("Please enter an Integer, Try Again!!")
    elif(oper == '/'):
        print ("Division")
        try:
            print ( (lambda x,y: x / y) ( int(input("First Number: ")), int(input("Second Number: ")) ))
        except ZeroDivisionError:
            print ("Zero Division Error: Division by Zero not Possible")
        except ValueError:
            print ("Please enter an Integer, Try Again!!")
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