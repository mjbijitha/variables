for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("yes,free is present")

#check if not

print("expensive" not in txt)
if "expensive" not in txt:
    print("yes,expensive is not pressent")

#slicing

b="JAVASCRIPT" #get the characters 2 to 5(not included)
print(b[2:5])
print(b[1:6])
print(b[:5]) #slicing from the start
print(b[1:]) #get the characters to the end
print(b[-5:-2])

a="windows"
print(a.upper())
print(b.lower())
c=" My ,name ,is,Bijitha, and ,Im ,a civil ,  engineer "
print(c.strip())
d="helo,world!"
print(d.replace("h","j"))
print(d.replace("he","me"))
print(d.split(","))
print(c.split(','))