"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

#Option 1
def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR

#Option 2
def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR

#Option 3
def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)

#Option 4
def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / credits

#Option 5
def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    semester_cost = credit_cost * CS1430_CREDITS
    return semester_cost / CS1430_MEETINGS_PER_SEMESTER

#Option 6
def cost_per_minute(annual_cost, credits):
    """Calculate the cost per minute."""
    return cost_per_class(annual_cost, credits) / 50



# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college:"))
    credits = int(input("Credits this semester: "))

    while True:
        print("\nTHE COST OF COLLEGE")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost per minute")
        print("Q. Quit")

        choice = input("Choose an option: ")

        
        if choice == "1":
            amount = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${amount:.2f}")
        elif choice == "2":
            amount = cost_per_month(annual_cost)
            print(f"Cost per month: ${amount:.2f}")
        elif choice == "3":
            amount = cost_per_day(annual_cost)
            print(f"Cost per day: ${amount:.2f}")
        elif choice == "4":
            amount = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${amount:.2f}")
        elif choice == "5":
            amount = cost_per_class(annual_cost, credits)
            print(f"Cost per class: ${amount:.2f}")
        elif choice == "6":
            amount = cost_per_minute(annual_cost, credits)
            print(f"Cost per minute: ${amount:.2f}")
        elif choice == "Q":
            print("Thanks for running the numbers!")
            break
        else:
            print("Invalid option. Please try again.")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
