text="ice cream"
#Accessing string character wise
print(text[0])

#Strings are immutable
try:
    updated_str=text[0]='a'
    print(updated_str)
except:
    print("String are immutable cannot be modified")

#Subindex
print(text[0:3])
print(text[4:9])
print(text[4:])
print(text[:3])

#Multiline string
Address='''
    Air force station, Shillong, 
    Near Laitkor Peak, Meghalaya, 
    793010
'''
print(Address)

#Joining 2 strings
str1="Hello"
str2="World"
print(str1+' '+str2)