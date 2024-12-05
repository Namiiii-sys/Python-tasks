#1) To print the sum of all numbers between m and n (both included), using for loops (m and n are user-defined inputs)
m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
sum=0
for i in range(m,n+1):
    sum+=i
print("The sum of numbers between",m,"and",n,'is:',sum)

#2) To take two numbers from the user and check if one number perfectly divides the other.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a%b==0:
    print("b perfectly divides a")
elif b%a==0:
    print("a perfectly divides b")
else:
    print("Not a perfect division")

#3) To print the area and perimeter of a circle if the diameter is given by the user.
diameter=int(input("enter the Diameter: "))
r=diameter/2
print("The perimeter of the circle is:",2*3.14*r)
print("The Area of the circle is:",3.14*r*r)

#4) To print the factorial of a number given by the user.
N=int(input("Enter the number to find factorial: "))
fact=1
for i in range(1,N+1):
  fact*=i

print(fact)
  
#5) To print the following pattern : 

for i in range(1,7):
    for j in range(1,i):
        print(j, end="")
    print()