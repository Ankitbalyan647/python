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
set.add(3)
set.add(4) 
set.remove(2)
print(set)