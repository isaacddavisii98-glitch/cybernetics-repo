# interest_calculation.py


while True:
    try:
     investment = int(input("Enter the investment amount (greater than 0 and less than 50000): "))
     if investment > 0 and investment < 50000:
         break
     else:
         print("Invalid amount. Please try again.")
    except ValueError:
     print("Please enter a valid number.")


while True:
    try:
        rate = float(input("Enter the interest rate (greater than 0 and less than 15): "))
        if rate > 0 and rate < 15:
            break
        else:
         print("Invalid rate. Please try again.")
    except ValueError:
     print("Please enter a valid number.")


while True:
    try:
        years = int(input("Enter the investment duration in years (greater than 0): "))
        if years > 0:
            break
        else:
         print("Invalid duration. Please try again.")
    except ValueError:
        print("Please enter a valid number.")


months = years * 12
monthly_rate = (rate / 100) / 12


current_value = investment

for month in range(1, months + 1):
   
    current_value += current_value * monthly_rate

    
    if month % 12 == 0:
     print(f"Year {month // 12}: ${current_value:,.2f}")


print(f"\nInvestment Summary:")
print(f"Initial Investment: ${investment:,.2f}")
print(f"Years: {years}")
print(f"Interest Rate: {rate}%")
print(f"Final Value after {years} years: ${current_value:,.2f}")

print("\nCompleted by [Isaac Davis]")