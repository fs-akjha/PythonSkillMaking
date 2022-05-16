items=["bread","pasta","fruits","veggies"]
print(items)

#Checking by index
print(items[1])

#Modifying List
#chips instead of bread
items[0]='chips'
print(items)

#Accessing range of items
print(items[0:2])
print(items[-1])
#Appending element
items.append("butter")
print(items)
#Inserting element at particular address
items.insert(1,'butter')
print(items)

#Joining 2 lists
food=['bread','pasta','fruits']
bathroom=['shampoo','soap']
item=food+bathroom
print(item)

#Lists cannot be concatenated by str or number

#Checking length of List items
print(len(item))

#Use of in operator in Lists

print("bread" in item)
print("milk" in item)