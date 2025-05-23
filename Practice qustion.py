# qus: 1
frist = int(input ("Frist number:" ))
second = int(input ("Second number:" )) 
print ("sum =", frist + second) 
# qus: 2
side = int(input("Enter the length of side of square: "))
area = side * side
print("Area of the square is:", area)   
# qus: 3
a = float(input ("frist number :"))
b = float(input ("second number :")) 
print ("avg =", (a+b)/2)
# qus: 4
a = int(input ("frist number :"))
b = int(input ("second number :"))
print (a>=b)
# qus: 5
a = int(input ("enter a number: "))
if (a%2==0):
    print ("even")
else:
    print ("odd") 
# qus: 6
a = int(input ("enter a number A: "))
b = int(input ("enter a number B: "))
c = int(input ("enter a number C: "))
if (a>b) and (a>c):
    print ("a is greatest")
elif (b>a) and (b>c):
    print ("b is greatest")
else:
    print ("c is greatest")
# qus: 7
a = int(input ("enter a number: "))
if (a%7==0):
    print ("Number is multiple of 7")
else:
    print ("Nummber is not multiple of 7")
# qus: 8
movies = []
movies.append(input("Enter 1st movie name: "))
movies.append(input("Enter 2nd movie name: "))
movies.append(input("Enter 3rd movie name: "))
print("Movies:", movies)

# qus: 9
list1 = [1,2,1]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("List1 is palindrome")
else:
    print("List1 is not palindrome")

# qus: 10
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))
 
# qus: 11
tup = ["C","D","A","A","B","B","A"]
tup.sort()
print(tup)

# qus: 12
list= {
    "table" : "a piece of furniture", "list of facts & figures"
    "cat" : "a small animal"
}
print(list)

# qus: 13
classroom = {"python", "java", "c++", "python", "javascript","java", "python","java", "c++", "c"}
print(classroom)
print(len(classroom))

# qus: 14
dict = {}
dict["Math"] = 89
dict["English"] = 78
dict["Hindi"] = 90
print(dict) 
# or
marks = {}
x = int(input("enter marks of Math: "))
marks.update({"Math": x})
y = int(input("enter marks of English: "))
marks.update({"English": y})
z = int(input("enter marks of Hindi: "))
marks.update({"Hindi": z})
print(marks)

# qus: 15
list = {9, "9,0"}
print(list)
# or
list = {
    ("float", 9.0),
    ("int", 9),
}
print(list)
