


DAY7


##Write a program that computes and prints the result of 512 − 282/47 · 48 + 5. (It is roughly .1017)
a=512
b=282
c=47
d=48
e=5
print((a-b)/(c*(d+e)))
0.0923323966278603

##write a program that ask the user to enter the number. print out the square but use the optional argument to print it out in a full sentence . enter the number: 5
##the square of 5 is 25
a=int(input("Enter the number : "))
print("the square of "+ str(a)+" is "+str(a**2))
Enter the number : 4
the square of 4 is 16

##write a program that ask the user to enter a number x and then use the sep optional argument to print out 2x 3x 4x each should be seprated with 3 dashes
a=int(input("Enter the number : "))
print(str(a)+"---"+str(2*a)+"---"+str(3*a)+"---"+str(4*a)+"---"+str(5*a))
Enter the number : 4
4---8---12---16---20

##. Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.
a=int(input("enter the weight in kilogram : "))
b=a*2.2
print("there are 2.2 pounds in a kilogram "+str(b))
enter the weight in kilogram : 4
there are 2.2 pounds in a kilogram 8.8

##Write a program that asks the user to enter three numbers (use three separate input state- ments). Create variables called total
## and average that hold the sum and average of the three numbers and print out the values of total and average
a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))
f=(a+b+c)
print("the sum of 1st 2nd 3rd is "+str(f))
d=(a+b+c)/3
print(" average is : "+str(d))
enter the first number2
enter the second number2
enter the third number2
the sum of 1st 2nd 3rd is 6
the sum of a b c and their average is : 2.0

##A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and the percent tip they want to leave.
## Then print both the tip amount and the total bill with the tip included.
a=int(input("enter the rate of the meal"))
b=int(input("enter the percent tip"))
c=a*(b)/100
print(c)
enter the rate of the meal500
enter the percent tip5
25.0