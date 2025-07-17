name = "sahib"
age = 18
price = 24.99
gf = False
job = None

age2 = age

print(name)
print(age)
print(price)

print("my name is: ", name ,"my age :" , age2 )


#or


print("my name is: ", name )
print("my age: ", age2)


#Types


print(type(name))
print(type(age))
print(type(price))
print(type(gf))
print(type(job))


#sums


a = 2
b = 5
sum = a + b
print(sum)



#INPUTS



name = input("name : ")
print(name)

age = int(input("your age: "))
print(age)

price = float(input("what is pen price: "))
print(price)

#or

name = input("name : ")
age = int(input("age: "))
price = float(input("pen price: "))

print("my name is: " , name , "and my age is:" , age , ",my pen price is:" , "$" ,price)



#Conditional Statements



light = input("light color : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("Light is Broken")