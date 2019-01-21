# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:37:57 2019

@author: thanusha
"""
#problem statement 1.1
class Area:          #parent class
    def _init_(self): #constructor
        pass
    def Input(self):   # defining function
        self.p =float(input("enter the side 1 : " ))
        self.q =float(input("enter the side 2 : " ))
        self.r =float(input("enter the side 3 : " ))
        
class Triangle(Area):   #child class
    def _init_(self):     
        super()._init_(self) #referring parent class from child
    def FindArea(self):     #defining function
        a=self.p
        b=self.q
        c=self.r
        s=((a+b+c)/2)       #perimeter calculation
        area=(s*(s-a)*(s-b)*(s-c))**0.5  # area calculation
    
        print("the area of the triangle is : ", area) #print the area
           
        
t= Triangle()    #object created for child class
t.Input()        # calling parent class method
t.FindArea()     #calling child class method

#problem statement 1.2
n =int(input("Enter the integer: "))      # taking input from user
words= input("Enter the list of words: ").split(',') # taking input from user and spliting based on commas entered
new_list =[]     # created a new empty list

def filter_long_words(words,n): #defining the function filter_long_words with list and interger as parameters
    
    

    for x in words:       #iterating through list
        
        y=len(x)            # y is assigned with length of each string in the list
        
        if y>n:          # using if condition if length of each string is greater than entered integer
            new_list.append(x)  #add the element to the empty list using append method
    return new_list       # return the list
        

filter_long_words(words,n) #function call
print(new_list)           # print the returned list

#problem statement 2.1
words= input("Enter the list of words: ").split(',')
new_list =[]
def number_list(words):
    for x in words:       #iterating through list
        y= len(x)               # y is assigned with length of each string in the list
        new_list.append(y)     #add the length of each element to the empty list using append method
    return new_list       # return the list
        
print(number_list(words)) # function call and printing the return value of the function

#problem statement 2.2
character= input("enter a character :")  # taking a character from user

def isvowel(character):    # function defination
    if character in ('a','e','i','o','u','A','E','I','O','U'):  #checking whether character is upper case or lower case vowel
       return True
    else:
       return False

print(isvowel(character))  #function call and printing the return value of the function





   
        