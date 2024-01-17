import math

choose_calculation=(input('''investment - to calculate the amount of interest you'll earn on your investment

bond - to calculate the amount you'll have to pay on a home loan

Enter either "investment" or "bond" from the menu above to proceed: ''')).lower()



if choose_calculation  != "investment" or choose_calculation != "bond":
    print("Please enter a valid value")
    
    

if choose_calculation == "investment": # Use lower to make output lowercase
    user_amount=int(input("Please enter the amount of money deposited: "))
    user_interest=int(input("Please enter desired interest rate: "))
    user_years_investment=int(input("Please enter the number of years you want to invest for: "))
    interest_type=(input("Please enter 'simple' or 'compound' interest: ")).lower()
    
elif choose_calculation == "bond":
    house_value=int(input("Please enter the present value of the house: "))
    house_interest=int(input("Please enter the interest rate for your house bond: "))
    house_months=int(input("Please enter the number of months to repay the bond: "))
   
# Calculate interest for investment
if choose_calculation == "investment" and interest_type == "simple":
        simple_interest=user_amount*(1 + (user_interest/100)*user_years_investment)
        print(f"Your interest is {simple_interest}")
    
elif choose_calculation == "investment" and interest_type == "compound":
    compound_interest=user_amount*math.pow(1 + (user_interest/100),user_years_investment)
    print(f"Your interest is{compound_interest}")
    

    
# Calculate bond repayment

if choose_calculation == "bond":
    bond_repayment=(((house_interest/100)/12)*house_value)/(1-(1+((house_interest/100)/12))**(-house_months))
    print(f"Your bond repayment value is {bond_repayment}")