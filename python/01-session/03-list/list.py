#---create list----
names=["Piyumal","saman","chamara"]
numbers=[10,20,30,40,50]


#---print list----
print(names)
print(numbers)

print("---------")
print(names[1])
print(names[2])


#---Add list values for end----
names.append("sadun")
print(names)

#---Add list values for start----
names.insert(0,"malith")
print(names)



#---remove list values----
names.pop(0)
print(names)


#---Update list values----
names[1]="sandaruvan"
print(names)


#---number of values----
amount=len(names)
print("Amount of names : "+str(amount))