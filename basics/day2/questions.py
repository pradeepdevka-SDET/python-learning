 #Q1 : nums = [1,2,3,4,5] print all numbers

nums = [1,2,3,4,5]

for i in nums:
    print(i)

#Q2 nums = [1,2,3,4,5] print even numbers
print("Even numbers:")
for i in nums:
    if i%2==0:
        print(i)

#Q3 nums = [10,20,30] find sum
nums = [10,20,30]
sum=0
for i in nums:
    sum+=i
print(sum)

# student = {
#     "name":"Pradeep",
#     "city":"Bengaluru"
# }
#
# print all keys

student = {
    "name":"Pradeep",
    "city":"Bengaluru"
}

print(student.keys())


