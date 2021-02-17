x="awesome"
print("Python is "+x)
y="youtube"
print(y + "rocks")
x="python is "
y=" awesome"
z=x+y
print(z)
#global variable-variable which are created outside the function


#create a variable outside and use inside a fuction

x="awesome"
def myfunc():
    print("python is "+x)
myfunc()

#create a variable inside a fuction,with the same name as the global variable

x="awesome"
def my_func():
    x="fantastic"
    print("python is "+x)
my_func()

print("python is "+ x)


#global keyword -used to create global variable inside a fun

def my_fun():
    global x
    x= "fantastic"
my_fun()
print("python is " + x)
