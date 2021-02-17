thistuple=("apple","banana","cherry")
print(thistuple)
#tuple allows duplicate value
thistuple=("apple","banana","cherry","apple","kiwi")
print(thistuple)
print(len(thistuple))


#to create tuple with one item ,put comma
thistuple=("apple",)
print(type(thistuple))
#accessing element
thistuple=("apple","banana","cherry","apple","kiwi")
print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#index 2 included,5 not included
print(thistuple[:4])
print(thistuple[2:])

#check if item exists
thistuple=("apple","banana","cherry")
if "apple" in thistuple:
    print("yes,it is in this tuple")

for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1

#join tuples
tup1=("a","b","c")
tup2=("1","2","3")
tup3=tup1+tup2
print(tup3)

#multiply tuples
tup4=tup1*2
print(tup4)

