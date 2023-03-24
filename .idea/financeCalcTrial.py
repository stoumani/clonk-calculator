import math

def compound_interest(initial_balance, interest_rate, periods_per_year, num_years):
    """
    Calculate the total compound interest for a given initial balance, interest rate, number of times interest
    is applied per period, and number of periods.
    """
    if initial_balance <= 0 or interest_rate <= 0 or periods_per_year <= 0 or num_years <= 0:
        print("Error: Invalid input. All values must be greater than zero.")
        return None
    
    total_periods = periods_per_year * num_years
    interest_rate_per_period = interest_rate / periods_per_year
    compound_interest = initial_balance * (1 + interest_rate_per_period) ** total_periods - initial_balance
    return compound_interest

def simple_interest(initial_balance, interest_rate, num_years):
    """
    Calculate the total simple interest for a given initial balance, interest rate, and number of years.
    """
    if initial_balance <= 0 or interest_rate <= 0 or num_years <= 0:
        print("Error: Invalid input. All values must be greater than zero.")
        return None
    
    simple_interest = initial_balance * interest_rate * num_years
    return simple_interest

def interest_percentage(interest, principal):
    """
    Calculate the interest percentage for a given interest and principal amount.
    """
    if interest <= 0 or principal <= 0:
        print("Error: Invalid input. Interest and principal amounts must be greater than zero.")
        return None
    
    interest_percentage = (interest / principal) * 100
    return interest_percentage

# Example usage
initial_balance = 1000
interest_rate = 0.05
periods_per_year = 12
num_years = 5
compound_interest_total = compound_interest(initial_balance, interest_rate, periods_per_year, num_years)
print(f"Total compound interest: {compound_interest_total:.2f}")

initial_balance = 5000
interest_rate = 0.03
num_years = 10
simple_interest_total = simple_interest(initial_balance, interest_rate, num_years)
print(f"Total simple interest: {simple_interest_total:.2f}")

interest = 500
principal = 10000
interest_percent = interest_percentage(interest, principal)
print(f"Interest percentage: {interest_percent:.2f}%")
