#PYTHON HOMEWORK ASSIGNMENT 5
'''
Author         : Dinesh
published Date : 26-01-2019
'''

#check whether given number is prime or not if number is prime prime return true otherwise false
def isPrime(num,i=2):
    if num<=2:
        return True if num==2 else False
    if num%i==0:
        return False
    if i*i>num:
        return True
    return isPrime(num,i+1)


for num in range(1,101):
    if isPrime(num)==True:    #prime or not
           print('Prime')
    else:
            #the number is divible by both 3 and 5
            if num%3==0 and num%5==0: 
                  print('FizzBuzz')
            #the numebr is only divisible by 3
            elif num%3==0:
                  print('Fizz')
            #the number is only divisible by 5
            elif num%5==0:
                   print('Buzz')
            #otherwise print that number
            else:
                print(num)
