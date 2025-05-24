#function defibation
def add(a, b):
    sum = a + b
    print (sum)
    return sum


add (75,75)
add (100, 200)
def print_hello():
    print("Hello, World!")

print_hello()
def calc_avg(a, c, b):
    SUM = a + b + c
    avg = SUM / 3
    print("The average is:", avg)
    return avg

calc_avg(10, 20, 30)

# qus 1
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
heroes = ["Superman", "Batman", "thor", "Ironman", "Hulk"]
def print_len(list):
    print("The length of the list is:", len(list))
    
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print_len(cities)

# qus 2
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(7)

# qus 3
def conv(usd):
        inr = 82.73
        print("inr=", usd*inr)
conv(56)