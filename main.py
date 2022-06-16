print("Welcome to the tip calculator!")

total_sum = float(input("What was the total bill? €"))
tip = int(input("How much tip would like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_incl_tip = (((total_sum) * tip)/100)*10
price_per_person = total_incl_tip / people

result = "%.2f" % round(price_per_person,2)

print(f"Each person should pay €{result}.")