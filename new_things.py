def calu():
        a = int(input("enter a number"))
        s = input("enter your sing")
        if s == "+":
                b = int(input("enter your another number:"))
                sum = (a+b)
                print("your result is:", sum )
        elif s == "*":
                b = int(input("enter your another number:"))
                mult = (a*b)
                print("your result is:", mult)
        elif s == "/":
                b = int(input("enter your another number:"))
                div = (a/b)
                print("your result is:", div )
        elif s == "-":
                b = int(input("enter your another number:"))
                sub = (a-b)
                print("your result is:", sub)
        print ("end")

calu()
