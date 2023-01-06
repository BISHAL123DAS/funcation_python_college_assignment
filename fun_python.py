#1. Create a function to print your name using Python.
# def my_funcation():
#     print('python programing language')
# my_funcation()    

#2. Write a program to add two integers using function.
# def my_funcation():
#     c=a+b
#     print(c)
# a,b=map(int,input('enter your number:').split())
# my_funcation()

#3. Create a function to multiply two numbers and the numbers should pass as parameter
#and return the result.

# def funcation(a,b):
#     c=a*b
#     return c
# print("the summ is:")
# rest=funcation(4,5)
# print(rest)

#4. Write a Python program to access a function inside a function
# def my_funcation():
#     s='gekksy bishal'
#     def fun2():
#         print(s)
#     fun2()
# my_funcation()     

#5. Write a Python program to understand the use of global and  nannical variables
#declared in a function.
# s=52
# def fun():
#     print(s)
#     def fun2():
#         s=56
#         print(s)
#     fun2()
# fun()        



#6. Write a Python program to understand the use of asterisk(*) character declared in a
#function.
#7. Write a Python program to understand the use of asterisk(**) character declared in a
#function.


#8. Create a function to calculate and return LCM of two numbers
# def lcm(n1,n2):
#     big=n1>n2 and n1 or n2
#     while(1):
#         if(big%n1==0)and (big%n2==0):
#             return big
#             break
#         big+=1
# x,y=map(int,(input("enter your value:").split()))      
# result=lcm(x,y)  
# print(result) 

#9. Create a function to calculate and return HCF of two numbers.
# def hcm(a,b):
#     i=1
#     big=0
#     while i<=a and i<=b:
#         if(a%i==0 and b%i==0):
#             big=i
#         i+=1    
#     return big
# x,y=map(int,(input("enter your two variables:").split()))
# res=hcm(x,y)
# print(res)



#10. Write a Python function to find the max of three numbers.
# def bigest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
# res=bigest(4,15,6)
# print(res)   

# 11. Write a Python function to sum all the numbers in a list.
# def lsum(l):
#     sum=0
#     for i in l:
#         sum+=i
#     print(sum)  
# lsum(l=[45,65,11,23,4,56])

#12. Write a Python function to multiply all the numbers in a list
# def mul(l):
#     m=1
#     for i in l:
#         m*=i
#     return m
# res=mul(l=[5,4,3,5])
# print(res)

#13. Write a Python program to reverse a string.
# n='bishal'
# ns=''
# while(n!=''):
#     nss=n[-1]
#     ns+=nss
#     n=n[:-1]
# print(ns) 

# def revs(n):
#     r=''
#     while(n!=0):
#         p=n[-1]
#         r+=p
#         n=n[:-1]
#     return r 
# n=input('enter')
# res=revs(n)
# print(res)    

#14. Write a Python function to calculate the factorial of a number (a non-negative integer).
#The function accepts the number as an argument.
# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         return n* fact(n-1)
# print(fact(5))

# def fact(n):
#     fa=1
#     for i in range(1,(n+1)):
#         fa*=i
#     return fa
# res=fact(5)
# print(res)    

#15. Write a Python function to check whether a number falls in a given range.

# def checkrange(n):
#     if n in range(5,20):
#         print('%s in the raange'%str(n))
#     else:
#         print('not in present in the range') 
# n=int(input('enter your value:'))
# checkrange(n)           

#16. Write a Python function that accepts a string and calculate the number of upper case
#letters and lower case letters.

# def strings(n):
#     d={"uppercase":0,"lowercase":0}
#     space=0
#     for i in n:
#         if i.isupper():
#             d["uppercase"]+=1
#         elif i.islower():
#             d["lowercase"]+=1
#         else:
#             space+=1    
#     print('no of uppercase is',d["uppercase"]) 
#     print('no of lowercase',d["lowercase"])
#     print('the space is',space)
# n=input('enter your string:')
# strings(n)                


#17. Write a Python function that takes a list and returns a new list with unique elements of
#the first list.

# n=[4,5,6,7,7,7,8,8,9]
# i=0
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         if(n[i]==n[j]):    # this soluation some bugs are there...
#             n.remove(n[j])
#         j+=1
#     i+=1    
# print(n)


# def orgv(n):
#     s=[]
#     for i in n:
#         if i not in s:
#             s.append(i)
#     return s 
# res=orgv(n=[45,65,164,265,45,21,265,21,65,5])  
# print(res)     

#18. Write a Python function that takes a number as a parameter and check the number is
#prime or not.

# n=int(input("enter your value:"))
# flag=0
# i=2
# while i<n:
#     if(n%i==0):
#         flag=1
#         print('not prime')
#         break  
#     i+=1
# if(flag==0):
#     print('this is prime no:')    


# def prime(n):
#     i=2
#     fg=0
#     while i<n:
#         if(n%i==0):
#             fg=1
#             print("not prime")
#             break
#         i+=1
#     if(fg==0):
#         print("prime")  
# n=int(input('enter your value:'))
# prime(n)              

#19. Write a Python program to print the even numbers from a given list.
# def even(n):
#     l=[]
#     for i in n:
#         if(i%2==0):
#             l.append(i)
#     return l 
# res=even(n=[4,6,1,3,7,5,9,51,9])  
# print(res)     

#20. Write a Python function to check whether a number is perfect or not
# def perfectn(n):
#     sum=0
#     for i in range(1,n):
#         if(n%i==0):
#             sum+=i
#     if(sum==n):
#         print('perfect')
#     else:
#         print('not perfect')            
# n=int(input("enter your value:"))
# perfectn(n)




#21. Write a Python function that checks whether a passed string is palindrome or not


# n=int(input('enter your input:'))
# s=n
# sum=0
# while(n!=0):
#     rem=n%10
#     sum+=rem*rem*rem
#     n=n//10
# if(sum==s):
#     print('palindrome')
# else:
#     print('not palindrome')     

# n=input("enter your strongs:")
# z=n
# s=''
# while(n!=''):
#     p=n[-1]
#     s+=p
#     n=n[:-1]
# print(s)    
# if(s==z):
#     print('palindrome')
# else:
#     print('not plindrome')        


#22. Write a Python function to create and print a list where the values are square of
#numbers between 1 and 30 (both included)

# n=[45,12,5,346,9,64,4,6,87,4,7,5,1,29,30]
# l=[]
# for i in n:
#     if i in range(1,30+1):
#             l.append(i**2)
# print(l)          

# def checkval(n):
#     l=[]
#     for i in range(1,31):
#             l.append(i**2)
#     return l
# n=(input("enter your input:")).split()  
# nl=[int(i)for i in n]
# res=checkval(nl)
# print(res)
