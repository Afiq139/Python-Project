# BMI Calculator


# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

# The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

# Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

# Sample Input
# 85
# 1.9

# Sample Output
# Normal
# Weight is in kg, height is in meters.
# Note, that height is a float.

#your code goes here
weight=float(input())
height=float(input())

bmi=weight/(height**2)

if bmi<18.5:
  print('Underweight')
elif bmi>=18.5 and bmi<25:
  print('Normal')
elif bmi>=25 and bmi<30:
  print('Overweight')
else:
  print('Obesity')