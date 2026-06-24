nums=[1,2,3,2]

# append : Adds the element at the end of the list.
nums.append(40)
nums.append(678)

print(nums)

#remove : removes the first item with the specified values

nums.remove(678)
print(nums)

# nums.remove(5)

# pop(), pop(index) : removes the element at the specified position
# if only pop() then it removes the last indexed element
#if negative values passes, so it starts from the end

nums.pop(0)
nums.pop()
print(nums)

# insert(index,value) : adds the element in the specified position
# -1 : adds at then 2nd last index,
# for adding in last index use-> .insert(len(nums),500) or use append(500) or use any far index
# insert basically insert the element before this index, so if will pass insert(100,5) it will append at then end, if insert(-100,5) it adds at the beginning

nums.insert(0,50)
print(nums)

nums.insert(-1,100)
print(nums)

nums.insert(len(nums),500)
print(nums)
nums.append(500)
print(nums)

nums.insert(100,9)
print(nums)
nums.insert(-100,9)
print(nums)

# indexing starts with 0, -1 for the last index , -2 second last and so on

print(nums[0])

# sort : sorts the list in ascending order, if we need to sort it in descending .sort(reverse=True)
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# sort updates the list itself, and sorted function returns the sorted list
list1=sorted(nums)
print(list1)

# index : returns the index of first matching value

x=nums.index(100)
print(x)

# count : returns the number of elements with the specified value( occurrence of a value)
y=nums.count(1)
print(y)


# extend : Adds the element of a list at the end, where append treat it as a single object and adds it to the list
nums.append([-1,-2])
nums.extend([-1,-2])
print(nums)

letters=['a','b']
letters.append(["ab"])
letters.extend(["cd"])
letters.extend("ef")
print(letters)

# clear : removes everything from the list, removes all the elements from the list
nums.clear()
print(nums)


# without copy : if we assign one list to the another, and if we append/remove any thing so it will do changes in both the lists,
# Both variables points to the same list

a=[1,2,3]
b=a
b.append(4)

print(a)
print(b)
a.remove(1)
print(a)
print(b)

# with copy : in memory they are diff lists altogether

x=[1,2,3]
y=x.copy()

y.append(4)
print(x)
print(y)
x.remove(2)
print(x)
print(y)

print(nums)
nums.extend(y)
print(nums)







