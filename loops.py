# This script demonstrates the use of a while loop in Python.
# qus 1
i = 1
while i <= 100:
    print(i)
    i += 1
print("End of loop")

# qus 2
i = 100
while i >= 1:
    print(i)
    i -= 1
print("End of loop")

# qus 3
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
print("End of loop")

# qus 4
num = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(num):
    print(num[i])
    i += 1
print("End of loop")
# qus 5

heros = ["spiderman", "batman", "superman", "ironman"]
i = 0
while i < len(heros):
    print(heros[i])
    i += 1
print("End of loop")

# qus 6
num = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i < len(num):
    if(num[i]== x):
        print ("found at idx", i)
    else:
        print ("not found")
    i += 1
print("End of loop")

# qus 7
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print("End of loop")

# qus 8
num = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i < len(num):
    if(num[i]== x):
        print ("found at idx", i)
        break
    else:
        print ("not found")
    i += 1
print("End of loop")

# qus 9
i = 0
while i < 10:
    i += 1
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("End of loop")

# qus 10
i = 1
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1
print("End of loop")

# qus 11
i = 1
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i += 1
print("End of loop")

# qus 12
num = [1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i) 
print("End of loop")

# qus 13
num = (1,4,9,16,25,36,49,64,81,100,49)
x = 49

idx = 0
for i in num:
    if (i == x):
        print("found at idx", idx)
    idx += 1

# qus 14
for i in range(10):
    print(i)

# qus 15
for i in range(1, 10):
    print(i)

# qus 16
for i in range(1, 10, 3):
    print(i)

# qus 17
for i in range(1,101):
    print (i)

# qus 18
for i in range (100, 0, -1):
    print (i)

# qus 19
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

# qus 20
for i in range(5):
    pass
if i >5:
    pass
print ("some useful code")

# qus 21
n = int(input("Enter a number: "))
sum = 0
i =1
while i <= n:
    sum += i
    i += 1
print("total sum is =", sum)

# qus 22
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
   sum += i

print("total sum is =", sum)

# qus 23
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i 
print("factorial is =", fact)

# qus 24
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i 
    i += 1
print("factorial is =", fact)

