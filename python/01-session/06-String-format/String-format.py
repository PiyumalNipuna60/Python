name="piyumal"


#--string %s---
print("My name is " + name)
print("My name is %s"%name)  #print("My name is " + name)


age=21

#--int %d---
# print("My name is " + name + ". age is"+age)
print("My name is %s age is %d"%(name,age))


height=3.2

#--double %f---
print("My name is %s, age is %d, and also my height is %f"%(name,age,height))

print("My name is %s, age is %d, and also my height is %.1f"%(name,age,height))  #dashamastana adu karanna



#------tuple and list-----------

my_data1=["Nipuna",21,3.5]  # tuple(meke data venas karanna ba)
my_data2=("Nipuna",21,3.5)  #list(data venas karanna puluvan)

# print("My name is %s, age is %d, and also my height is %.1f"% my_data1)  #Error 
print("My name is %s, age is %d, and also my height is %.1f"% my_data2)  

