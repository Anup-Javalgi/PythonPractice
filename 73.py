# Exception Handling in python = An event interrupts the flow of a program
                                #  (ZeroDivisionError, TypeError, ValueError)
                                #  1). try 2). except 3). finally

try:
    num =int( input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("You cant divide by 0 idiot")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")
