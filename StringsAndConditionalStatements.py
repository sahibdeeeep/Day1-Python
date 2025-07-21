str1 = "This is a string. \n creating it in python."
str1 = "This is a string. \t creating it in python."

print(str1)



#Concatenation



a = "hello"
b = "world"

print(a + b)

#or

a = "hello"
b = "world"
sum = a + b

print(sum)



#length of string



str2 = "hello"
len2 = len(str2)
print(len2)

str3 = "world"
len3 = len(str3)
print(len3)

finalstr = str2 + " " + str3
print(finalstr)
print(len(finalstr))



#Indexing



str4 = "sahibdeep singh"
print(str4[0])


#SLICING


str4 = "sahibdeep singh"
print(str4[10 : 15])

#or

str4 = "sahibdeep singh"
print(str4[10 : len(str4)]) #len is used for printing the word till end.

#or

str4 = "sahibdeep singh"
print(str4[10 : ]) #By tying nothin after ":" still it will print till last
print(str4[ : 5]) #[0 : 5]


#Negetive Slicing


str5 = "apple"
print(str5[-3 : -1])




#String Functions




#str.endswith("")
str6 = "apple"
print(str6.endswith("le"))


#str.capitalize()
str =  "i am learning python before collage"
print(str.capitalize())

#if i want to do changes in real string
str =  "i am learning python before collage"
str = str.capitalize()
print(str)


#str.replace(" " , " ")
str7 = "i am learning javascript before collage"
print(str7.replace("javascript" , "python"))


#str.find("")


str8 = "i am learning python before collage"
print(str8.find("o"))


#str.count("")
str9 = "i am learning python before collage"
print(str.count("o"))