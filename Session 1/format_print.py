print("I have a book")

#adding a backlash for " "
print("I became \"best\" coder by printing 'previous' lines.")

#variable can be start with _, (a-z), (A-Z)
_cars=5
print(f"There are {_cars} are available.")

""" for raw print statement will print same as it is"""
print(r"c\users")

#vatiable
People1=5

#format method
print("There are {} cars and there are {} people.".format(_cars,People1))

#numeric formatting
pi=3.141592
print(f"the value of pi is {pi:.2f}")

#some example
formatter="{} {} {} {}"
print(formatter.format(1,2,3,4))

print(formatter.format("ram","has","good","character."))

#end

#sep
l="abcd"
for i in l:
    print(i,sep=",",end="")