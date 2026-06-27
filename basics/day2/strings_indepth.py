name="Pradeep"
city="Bengaluru"
print(name)
print(city)

# indexing []

print(name[0])

#string slicing []

word="Python"
print(word)
print(word[0:3])
print(word[2:50])
print(word[::-1])

# reversing a string
print(word[::-1])

#string methods , .lower(), .upper()

s="hello"
s=s.lower()
print(s.upper())
s=s.upper()
print(s)
print(s.lower())

# strip() : remove only heading/trailing spaces
s="   Prad eep  "
print(s.strip())
sentence="I love coding"
new=sentence.replace("coding"," python")
print(sentence)
print(new)

text="you me him his"
result=text.split()
print(result)

# join -> converts list->string
ans=" ".join(result)
print(ans)

email="pradeepsingh@gmail.com"
flag=email.startswith("pradeepsingh")
print(flag)

flag=email.endswith("@gmail.coms")
print(flag)

# find : returns the index of the first matching element, if not found returns -1
index=email.find('z')
print(index)

# count: returns the occurrence of the element

occ=email.count('e')
print(occ)


# palindrome

word="madam"

if word==word[::-1]:
    print("Yes Palindrome")
else:
    print("Not a planidrome")

# count vowels in a string

str="Pradeep Singh Devka"
count=0
for ch in str:
    if ch in "aeiou":
        count+=1

print("Vowels : ", count)

