import copy

#Question1:->Reverse the whole list using list methods.
list1=[1,2,3,4,5,6,7,8]
print("List is : ",list1)
l2=list1[::-1]
print("List after reverse is : ",l2)

#Question2:->Print all the uppercase letters from a string.
str1=input("Enter a string : ")
for i in str1:
    if i.isupper():
        print(i)

#Question3-->Split the user input on comma's and store the values in a list as integers.
list2=input("Enter a string")
print(list2.split(" "))
li1=[]
for i in range(0,len(list2)):
    li1.append(list2[i])
print(li1)

#Check whether a string is palindromic or not.
string1=input("Enter a string to check whether string is palindrome or not : ")
reverse_string=reversed(string1)
if(list(string1)==list(reverse_string)):
    print("String is Palindrome")
else:
    print("String is Not Palindrome")

#Question6:->Make a deepcopy of a list and
#write the difference between shallow copy and deep copy.
list01=[1,2,[3,4],5]
list02=copy.deepcopy(list01)
list01[2][0]=6
print(list01)
print(list02)

'''
SHALLOW COPY:->A shallow copy creates a new object which stores the reference of
the origional elements.so,a shallow copy does not create a copy of nested objects.
Instead it just copies the reference of nested objects.
This means,a copy process does not recurse or create copies of nested
objects itself.

DEEP COPY:->A deep copy creates a new object and recursively adds the copies of
nested objects present in the original elements.
The deep copy creates independent copy of original object and all its nested objects.
'''





















doesn't 
