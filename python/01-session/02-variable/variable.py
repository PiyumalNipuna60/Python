

# String
name="Piyumal"
print("My name is : "+name)


# int
x=10
print(x)

# double
age=21 ,60.2
print(age)


# --------------
# casting
# int --> float {float()}
# float --> int {int()}
# int --> string {str()}
# int/string/float --> int {eval()}




x=20
weight=65.2
y="30"
#print("My Age is : "+x)  # wrong(Cast karanna one)
print("My Age is : "+str(x))

print("----------")
print(float(x))
print("Age Cast Flote : "+str(float(x)))

print(int(weight))
print("weight Cast int : "+str(int(weight)))

#eval
print(x*y) #error
print(x*eval(y))
