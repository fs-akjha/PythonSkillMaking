#Problem:- Store monthly expenses in a list and find out total expenses for all months

exp=[2340,2500,2100,3100,2980]
total=0
#Range Function

for i in range(len(exp)):
    print('Month: ',(i+1),'Expenses: ',exp[i])
    total=total+exp[i]

print("Toal expenses is: ",total)

#Problem:- Search for lost car key in home and when found stop searching
print('---------------------------------------------------------------------------------------------')
key_location='chair'
locations=['garage','living room','chair','closet']

for i in locations:
    if i==key_location:
        print("Keys found in ",i)
        break
    else:
        print("Keys not found in, ",i)


print('--------------------------------------------------------------------------------------------')
#Print square of numbers between 1 to 5 except even numbers

for num in range(1,6):
    if num %2!=0:
        print(num * num)
    continue