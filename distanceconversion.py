#Write a program to read distance value in meters and convert it into centimeters, inches, and yards.

d = int(input("Enter distance in meter: "))
d_centi = d * 100
d_inches = d * 39.37
d_yards = d * 1.094
print("The distance in miles is ", d_centi)
print("The distance in inches is ", d_inches)
print("The distance in yards is ", d_yards)
