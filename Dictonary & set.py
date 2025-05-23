info = {
    "key": "value",
    "subjact" :["Python", "Java", "C++"],
    "topics" :("dic", "set", "list"),
    "name" :"Ankit",
    "age" :25,
    "is student" :True,
    "marks" :[ 34, 45, 542, 23, 45, 67, 89, 90],
}
info["name"] = "Bhavik"
info["surname"] = "Kadyan"
print(info)
print(info["key"])
print(info["subjact"])
print(info["topics"])
print(info["name"])

null_dict = {}
null_dict["name"] = "Ankit"
null_dict["age"] = 25
print(null_dict)

student = {
    "name": "Ankit",
    "subjects": {
        "Python": 90,
        "Java": 80,
        "C++": 85 
    }
}
print(student)
#set
collection = {1,2,3,2,3,"hello","world","world"}
print(collection)
print(type(collection))
print(len(collection))
print("hello" in collection)

set= set()
set.add(1)
set.add(2)
set.add(2)
set.add((1, 2, 3))
set.add("hello")
set.add(4) 
set.remove(2)
print(set)
print (len(set))
print(set.pop())

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = (set1.union(set2))
print(set3)
set4 = (set1.intersection(set2))
print(set4)

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