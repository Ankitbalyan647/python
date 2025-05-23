marks = [ 87,34,45,542,23,45,67,89,90]
print("marks:", marks)
print(len(marks))
print(marks[0])
print(marks[1])

students = ["Ankit",86, "Amit", 45, "Anil", 78, "Ajay", 90]
print("students:", students)
print(students[0])
students[0] = "Bhavik"
print(students)

tup = ("C","D","A","A","B","B","A")
print(tup.count("A")) 
print(tup.index("A"))

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