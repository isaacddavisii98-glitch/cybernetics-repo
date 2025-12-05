import locale
import math
from decimal import Decimal, ROUND_HALF_UP

# Try to set US locale for currency formatting 
try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except locale.Error:
    # Fallback to system default if needed
    locale.setlocale(locale.LC_ALL, "")


def format_currency(amount):
    """
    Format a number as US currency using locale.
    'amount' can be float or Decimal.
    """
    try:
        # Convert to float just for display formatting
        return locale.currency(float(amount), grouping=True)
    except Exception:
        # Fallback using f-string formatting 
        return f"${float(amount):,.2f}"


def get_monthly_income():
    """
    Ask the user for total monthly income.
    Uses try/except and raises custom ValueError messages
    for invalid entries (Chapter 8).
    """
    while True:
        try:
            income_str = input("Enter your total income: ")
            income = float(income_str)

            # Custom error for negative income 
            if income < 0:
                raise ValueError("Income cannot be negative.")

            return income

        except ValueError as e:
            # Shows the original error message plus custom text
            print(f"Invalid input: {e}. Please enter a valid income amount.")


def get_expenses_list():
    """
    Ask the user for a list of expenses.
    Repeats until the user enters 0.
    Uses try/except and custom errors for invalid values.
    """
    expenses = []

    while True:
        try:
            expense_str = input("Enter an expense amount (or 0 to exit): ")
            expense = float(expense_str)

            if expense < 0:
                raise ValueError("Expense cannot be negative.")

            if expense == 0:
                break

            expenses.append(expense)

        except ValueError as e:
            print(
                f"Invalid input: {e}. Please enter a valid expense amount or 0."
            )

    return expenses


def main():
    print("Welcome to the Simple Budget Tracker")
    print("------------------------------------")

    #  Get valid income (as float first)
    income = get_monthly_income()

    #  Get list of expenses (floats)
    expenses = get_expenses_list()

    #  Use Decimal for exact money values 
    income_dec = Decimal(str(income)).quantize(Decimal("1.00"), ROUND_HALF_UP)

    total_expenses_float = sum(expenses)
    total_expenses_dec = Decimal(str(total_expenses_float)).quantize(
        Decimal("1.00"), ROUND_HALF_UP
    )

    remaining_dec = (income_dec - total_expenses_dec).quantize(
        Decimal("1.00"), ROUND_HALF_UP
    )

    # Also show remaining budget rounded DOWN to whole dollars using math.floor
    remaining_whole = math.floor(float(remaining_dec))

    #  Output budget summary with formatted numbers 
    print("\nBudget Results:")
    print("-" * 30)
    print(f"{'Total Income:':<22}{format_currency(income_dec)}")
    print(f"{'Total Expenses:':<22}{format_currency(total_expenses_dec)}")
    print(f"{'Remaining Budget:':<22}{format_currency(remaining_dec)}")
    print(
        f"{'Remaining (whole $):':<22}"
        f"${remaining_whole:,.0f}"  # comma + no decimals
    )

    #  Output numbered list of expenses with currency formatting
    print("\nComplete Expense List")
    print("-" * 30)
    if len(expenses) == 0:
        print("No expenses were entered.")
    else:
        for index, expense in enumerate(expenses, start=1):
            # f-string with commas and 2 decimal places 
            print(f"{index:>2}. {format_currency(Decimal(str(expense)))}")


# Run the program
main()


print("Completed by, [Isaac Davis]")  
