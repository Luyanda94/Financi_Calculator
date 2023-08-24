import math

def calculate_investment(principal, rate, time, simple_compound):
    r = (rate / 100) / 12

    if simple_compound == "simple":
        total = principal * (1 + r * time)
    else:
        total = principal * math.pow((1 + r), time)
    
    return total

def calculate_bond(pri, interest_rate, num_months):
    i = ((interest_rate / 100) / 12) / 12
    monthly_repayment = (i * pri) / (1 - math.pow(1 + i, -num_months))
    return monthly_repayment

print("Select an option:\n1. Investment\n2. Bond")
inv_bond = input("Enter 'Investment' or 'Bond': ").lower()

if inv_bond == "investment":
    principal = float(input("Enter principal amount for investment: "))
    rate = float(input("Enter interest rate: "))
    time = float(input("Enter duration for investment in years: "))
    simple_compound = input("Select 'Simple' or 'Compound' interest: ").lower()

    interest_earned = calculate_investment(principal, rate, time, simple_compound)
    print(f"Interest earned over {time} years: {interest_earned:.2f}")
elif inv_bond == "bond":
    pri = float(input("Enter the current value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    num_months = float(input("Enter the duration in months: "))

    monthly_repayment = calculate_bond(pri, interest_rate, num_months)
    print(f"Monthly repayment: {monthly_repayment:.2f}")
else:
    print("Enter a valid input.")
