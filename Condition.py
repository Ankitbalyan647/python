marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80):
    print("Grade B")
elif(marks >= 70):
    print("Grade C")
elif(marks >= 60):
    print("Grade D")
elif(marks >= 33):
    print("Grade E")
else:
    print("Grade F", "You are fail")

# qus: 9
list1 = [1,2,1]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("List1 is palindrome")
else:
    print("List1 is not palindrome")
