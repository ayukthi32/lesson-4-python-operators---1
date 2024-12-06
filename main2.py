#activity2
english = int(input("Enter marks for english"))
maths = int(input("Enter marks for maths"))
hindi = int(input("Enter marks for hindi"))
science = int(input("Enter marks for science"))
social = int(input("Enter marks for social"))

sum = english + maths + hindi + science + social

print("The sum of the marks:" , sum)

percentage = (sum/500) * 100
print("The percentage is:", percentage)