#Read the amount and percentage of interest from the keyboard and find final amount after adding interest in original amount.

amt = int(input("Enter amount: "))
per = int(input("Enter percentage of interest: "))
interest = (amt  * per) / 100;
finalamt = amt + interest
print("final amount after adding interest in original amount is:",finalamt)
