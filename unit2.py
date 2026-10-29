#30
'''
n=int(input())
for i in range(1,n):
    print(i)
    '''
#31
'''
n=int(input())
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)
'''
#32
'''
n=int(input())
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reverse=",rev)
'''
#33
'''
n=int(input())
for i in range(1,11):
    print(F"{n}*{i}={n*i}")
    '''
#34
'''
n=int(input())
fact=1
for i in range (1,n+1):
    fact=fact*i
print(f"factorial ={fact}")
'''
#35
'''
n=int(input())
for num in range(2,n+1):
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count=count+1
        if count==2:
            print(f"{num}")
            '''
#36
'''
n=int(input())
largest=0
for i in range(n):
    num=int(input("enter the number"))
    if num>largest:
        largest=num
print(f"largest={largest}")
'''
#37
'''
n=int(input("values"))
total=0
for i in range(n):
    num=float(input("numbers"))
    total=total+num
average=total/n
print("sum=",total)
print("average=",average)
'''
#38
'''
n=int(input())
a=0
b=1
for i in range(n):
    print(f" {a} ")
    c=a+b
    a=b
    b=c
    '''
#39
'''
n=int(input())
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if sum==temp:
    print("armstrong")
else:
    print("not armstrong")
    '''
#40
'''
n=int(input())
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("palindrone")
else:
    print("not parlidrone")
    '''
#41
''''
n=int(input())
i=1
while i<=10:
    print(f"{n}*{i}={n*i}")
    i=i+1
    '''
#42
'''
n=int(input())
count=0
while n>0:
    n=n//10
    count=count+1
print(f"{count}")
'''
#43
'''
for i in range (1,11):
    if i==5:
        break
    print(f"{i}")
    '''
#45
'''
for i in range (1,6):
    if i==3:
        pass
    print(f"{i}")7
    
'''
#46
'''
n=int(input())
for i in range(1,n+1):
    print(f"{'*'*i}")
    '''
#47
'''
n=int(input())
for j in range (n,0,-1):
    print(f"{'*'*j}")
    '''
#48
'''
n=int(input())
for i in range (1,n+1):
    space=" "*(n-i)
    numbers=" "
    for j in range(1,i+1):
        numbers=numbers+f"{j}"
        print(f"{space}{numbers}")
        '''
#49
'''
n=int(input())
for i in range (1,n+1):
    spaces=" "*(n-i)
    stars="*" *(2*i-1)
    print(f"{spaces}{stars}")
for i in range (n-1,0,-1):
    spaces=" " *(n-i)
    stars="*" * (2*i-1)
    print(f"{spaces}{stars}")
    '''
#50
'''
n=int(input())
for i in range(n):
    num=1
    spaces=" " *(n-i-1)
    row=" "
for j in range(i+1):
    row=row+f"{num}"
    num=num*(i-j)//(j+1)
    print(f"{spaces}{row}")
    '''
#51
'''
n=int(input())
num=1
for i in range(1,n+1):
    row=" "
    for j in range(1,n+1):
        row=row+f"{num}"
        num=num+1
        print(f"{row}")
        '''
#52
'''
str1="hello"
str2="world"
print(str1)
print(str2)
print(str1 + " " + str2)
print(str1*3)
print(str2[0:3])
'''
#53
'''
text="hello python world"
print(text.upper())
print(text.lower())
sentence="apple banana mango"
print(sentence.split())
words=["hello","python"]

print(sentence.replace("bananna","orange"))
print(sentence. find("mango"))
'''
#54
'''
text=input("enter")
if text==text[::-1]:
    print("jyo")
else:
    print("lokesh")
    '''
#55
'''
text=input()
reverse_text=text[::-1]
print(text)
print(reverse_text)
'''
#56
'''
text=input()
vowels=0
consonants=0
digits=0
spaces=0
for ch in text:
    if ch.lower() in "aeiou":
         vowels+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isalpha():
        consonants+=1
    elif ch==" ":
        spaces+=1
print(vowels)
print(consonants)
print(digits)
print(spaces)
'''
#57
'''
name=input()
age=int(input())
print(name)
print(age)
print(f"{name} {age}")
'''
#58
text=input()
for ch in dict from keys(text):
    print(text.count(ch))

    
