while True:
    first = input("Enter number or q to quit: ")
    if first.lower()=="q":
        print("Goobye!")
        break
    try:
        a=int(first)
        b=int(input("Enter second number: "))
        o=input("Enter operation +,-,*,/: ")
        match o:
            case"+":
                print(f'{a+b}')
            case"-":
                print(f'{a-b}')
            case"*":
                print(f'{a*b}')
            case"/":
                print(f'{a/b}')
            case _:
                print(f'invalid value try again!')
    except ValueError:
        print("invalid value try again!")
    except ZeroDivisionError:
        print("number cannot be divided by zero try again!")