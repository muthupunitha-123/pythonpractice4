#Odd or Even
n=int(input("Enter a number"))
if n&1:
  print("The number is odd")
else:
  print("The number is Even")
output:
Enter a number26
The number is Even


#CGPA
num=int(input("Enter a CGPA:"))
dep=input("Enter a department:")
if (num>=8 and dep=="IT"):
    print("Eligible for placement")
else:
    print("Not eligible for placement")
Output:
Enter a CGPA:7
Enter a department:IT
Not eligible for placement

#program for 5 table
n=int(input("Enter a table:"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)
output:
Enter a table:5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50

#program for print 5 and 7(prime number)
for i in range(5,8):
 if i==5 or i==7:
    print(i)
output:
5
7

#print each character of a string on seperate line
n=str(input("Enter a word: "))
for i in n:
 print(i)
output:
Enter a word: python
p
y
t
h
o
n

#find the length of the string
a=input("Enter a string:")
print("length of the string",len(a))
output:
Enter a string:python
length of the string 6

#find how many vowels are these in the string
n=input("Enter a string:")
count=0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print("vowels=",count)
output:
Enter a string:punitha
vowels= 3

#palindrome or not
a=input("Enter a word")
if a==(a[::-1]):
     print("palindrome")
else:
     print("not palindrome")
output:
Enter a word:madam
palindrome

#first and last character are same in the string
n=input("Enter s string:")
if n==0 and n==-1:
    print("same")
else:
    print("not same")
output:
Enter s string:hello
not same

#reverse character of a string
a=("hello")
print(a[0])
print(a[-1])
if(a[0]==a[-1]):
    print("character in a string")
else:
    print("not character in a string")
output:
h
o
not character in a string

#first non repeating characters in a string
s=("programming")
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break
output:
p

#Duplicate character in a string
s=input("Enter a string:")
print("Duplicate characters are:")
for ch in set(s):
    if s.count(ch)>1:
        print(ch)
output:
Enter a string:programming
Duplicate characters are:
m
r
g

#slicing
s=input("Enter the character:")
print(s[2:])
output:
Enter the character:python
thon

#calculate the length
s="python is programming language"
print(s.split())
print(s.count("length:",len(s)))
output:
['python', 'is', 'programming', 'language']
0

#find vowels and consonants
s=input()
vowels="aeiou"
consonants="bcdfghjklmnpqrstuvwxyz"
v=0
c=0
for i in s:
    if i in vowels:
     v+=1
    if i in consonants:
     c+=1
print(v,c)
output:
programming
3 8

#count words starting with a vowel
s=input().lower()
vowels="aeiou"
s=(s.split())
c=0
for i in s:
    i=i[0]
    if i in vowels:
        c+=1
print(c)
output:
an apple is on the table
4

#Anagram or not
a=input("Enter a first string:")
b=input("Enter a second string:")
if sorted(a)==sorted(b):
  print("Anagram")
else:
  print("not anagram")
output:
Enter a first string:silent
Enter a second string:listen
Anagram

#character counts
text=input("Enter a string:")
count={}
for ch in text:
  if ch in count:
        count[ch]+=1
  else:
        count[ch]=1
print("character counts:")
for ch,num in count.items():
 print(ch,":",num)
output:
Enter a string:python
character counts:
p : 1
y : 1
t : 1
h : 1
o : 1
n : 1

#angram using case methods
a=input()
b=input()
ch_a={}
ch_b={}
for i in a.lower():
    if i in ch_a:
        ch[i]+=1
    else:
        ch_a[i]=1
for i in b.lower():
     if i in ch_b:
        ch_[i]+=1
     else:
        ch_b[i]=1
if ch_a==ch_b:
     print("Anagram")
else:
     print("not anagram")
output:
silent
listen
Anagram

#convert upper case to lower case and lower case to upper case
s=input("Enter a string:")
result=""
for ch in s:
    if ch.isupper():
        result+=ch.lower()
    elif ch.islower():
        result+=ch.upper()
print("converted string:",result)
output:
Enter a string:pYThon
converted string: PytHON





















