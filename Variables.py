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



#Assignment Operator


num = 10
num = num + 10
print(num)

#or

num1 = 10
num1 += 5
print("num1:" , num1)



#logical Opereater



a1 = 50
b1 = 30
print(not (a > b))

val1 = True
val2 = False
print(val1 and val2)

print(val1 or val2)

print(a1 = b1 or a1 > b1)




#TypeConversion




a2 = int("2") #Even str value also converted into int but "word" can not be converted
b2 = 2.5
print(a2 + b2)


a3 = 2.5
b3 = str(a3)
print(type(a3))


val1 = input("name: ")
print(type(val1) , val1)