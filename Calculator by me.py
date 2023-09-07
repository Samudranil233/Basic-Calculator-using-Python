#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hello Welcome to this Calculator, This  calculator is made by Samudranil DUTTA...!!")
try:
    x = int(input("Enter your first number: "))
except ValueError:
    print("Sorry Wrong number..!! ")
try:
    y = int(input("Enter your second number: "))
except ValueError:
    print("Sorry its a wrong number..!!")
print("Thanks for this , now tell me which operation you want? Like *,/,+,-,%,//,** ")
try:
    op = input("Enter the operation: ")
except ValueError:
    print("Please provide a valid operation")

if (op == '+'):
    print(x + y)
elif (op == '-'):
    print(x - y)
elif(op == '%'):
    print(x % y)
elif(op == '*'):
    print(x * y)
elif(op == '/'):
    print(x / y)
elif(op == '//'):
    print(s // y)
elif(op == '**' ):
    print(x ** y)
else :
    print("Are you mad... Than sorry")


# In[ ]:





# In[ ]:





# In[ ]:




