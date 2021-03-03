# Write a program to read Celsius temperature and print equivalent Fahrenheit temperate on screen.Vice Versa

celsius = float(input('Enter temperature in Celsius: '))  
fahrenheit = (celsius * 1.8) + 32  #fahrenheit = (celsius * 9/5) + 32
print(celsius ,"Celsius is equal to" , fahrenheit , "degree Fahrenheit")  

fahrenheit = float(input('Enter temperature in Fahrenheit: '))  
celsius = (fahrenheit - 32) * 5/9  #celsius = (fahrenheit - 32) * 0.55
print(fahrenheit ,"Fahrenheit is equal to" , celsius , "degree Celsius")  
