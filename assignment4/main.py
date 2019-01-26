#PYTHON HOMEWORK ASSIGNMENT 4
'''
Author         : Dinesh
published Date : 26-01-2019
Description    : Create a function to make a list as unique
'''

#Globle variables
myUniqueList=[]
myLeftOvers=[]

#function definition
def uniquelist(element):
    if element not in myUniqueList:
        myUniqueList.append(element)
        return True
    else:
        leftovers(element)
        return False

def leftovers(element):
    myLeftOvers.append(element)

#Test cases
print(uniquelist('dinesh'))
print(uniquelist(10))
print(uniquelist('dinesh'))
print(uniquelist(20))
print(uniquelist(10))
print(myUniqueList)
print(myLeftOvers)