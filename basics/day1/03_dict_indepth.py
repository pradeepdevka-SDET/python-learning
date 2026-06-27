# dictionary stores the values in key: value pairs, list=[], tuple=(), dict={}

student={"name":"Pradeep","age":27,"place":"haldwani",5:2}
print(student)

# 01 accessing values

name=student["name"]
print(name)
age=student["age"]
print(age)

# 02 get is safer than [], why : [] it is expected that key is existed, if key doesn't exist we get an error : KeyError: 'names', while get would return 'None'

name=student.get("names")
print(name)
print(type(name))

# default value in get

name=student.get("names","Not available")
print(name)
print(type(name))

# 3. Adding a New Key

student["salary"]=5000
print(student)

# updating a value
student["salary"]=10000
print(student)

# pop : removes the element with a specified key

student.pop(5)
print(student)

# get all keys
keys=student.keys()
print(keys)

#get all values
values=student.values()
print(values)

# items : return a list containing a tuple for each key value pair
item=student.items()
print(item)

# loops thru a dictionary
for key,value in student.items():
    if key=="salary":
        student[key]=-500
        print(student.get(key))
    print(key,value)

print(student)

# check if key exists

flag="salary" in student
print(flag)

# copy
print("New code")

print(student)
#without copy
backup=student
backup.pop("salary")
print(student)
print(backup)
print("New code 2")

print(student)

studentCopy=student.copy()
studentCopy.pop("place")
print(student)
print(studentCopy)




# clear removes all the elements
student.clear()
print(student)





