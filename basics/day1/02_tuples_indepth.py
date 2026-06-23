person=("Pradeep",25,25)

 # Indexing : starts with 0
print(person[0])
print(person[1])


print(len(person))

# index(value) : it requires the element & return the index of that element

x=person.index("Pradeep")
print(x)
y=person.index(25)
print(y)

# count : return how many times a elements present in a tuple

n=person.count(25)
print(n)

