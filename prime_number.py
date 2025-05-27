def prime_no():
    n = int(input("enter a number:"))
    if n <= 1:
        print("it is not a prime number")
        return
    elif n % 2 == 0:
        print("it is not a prime number")
        return
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                print("it is not a prime number")
                return
        print("it is a prime number")

prime_no()