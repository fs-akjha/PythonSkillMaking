#Check if number is even or odd

num=input("Enter a number: ")
num=int(num)

if num %2==0:
    print("Number is even")
else:
    print("Number is odd")


#Write a program that asks user to enter a dish name and it should print which cuisine is that dish
indian_cu=['samosa','daal','Naan']
chinease_cu=['egg role','pot sticker','fried rice']
italian=['pizza','pasta','risoto']

dish_name=input("Enter a dishname: ")
if dish_name in indian_cu:
    print("Indian")
elif dish_name in chinease_cu:
    print("Chinease")
elif dish_name in italian:
    print("Italian")
else:
    print("Not sure")