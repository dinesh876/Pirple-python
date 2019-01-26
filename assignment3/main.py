#PYTHON HOMEWORK ASSIGNMENT 3
'''
Author         : Dinesh
published Date : 26-01-2019
Description    : Create a function that accepts 3 parameters and checks for equality between any two of them
'''
#Function definition

def comparison(a,b,c):
   a=int(a)
   b=int(b)
   c=int(c)
   if a==b or a==c or b==c:
       return True
   else:
       return False

#function calls
print(comparison(10,'10','5'))