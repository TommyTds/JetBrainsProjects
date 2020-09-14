from math import log, ceil
import argparse, sys

# write your code here
#step = input("""
#What do you want to calculate?
#type "n" for the number of months,
#type "a" for the annuity monthly payment,
#type "p" for the credit principal:
#""")

#def mode(step):
#    if step == "n":
#        credit_principal = float(input("Enter the credit principal: "))
#        monthly_payment = float(input("Enter the monthly payment: "))
#        credit_interest = float(input("Enter the credit interest: ")) / 100
#        
#        number_of_months(credit_principal, monthly_payment, credit_interest)
#        
#    elif step == "a":
#        credit_principal = float(input("Enter the credit principal: "))
#        number_of_periods = int(input("Enter the number of periods: "))
#        credit_interest = float(input("Enter the credit interest: ")) / 100
#        
#        annuity_monthly_payment(credit_principal, number_of_periods, credit_interest)
#        
#    elif step == "p":
#        annuity_payment = float(input("Enter the annuity payment: "))
#        count_periods = int(input("Enter the count of periods: "))
#        credit_interest = float(input("Enter the credit interest: ")) / 100
#        
#        count_credit_principal(annuity_payment, count_periods, credit_interest)

def number_of_months(credit_principal, monthly_payment, credit_interest):
    nominal_interes_rate = credit_interest
    count_periods = log(monthly_payment / (monthly_payment - nominal_interes_rate * credit_principal), 1 + nominal_interes_rate)
    count_periods = ceil(count_periods)
    overpayment = abs(credit_principal - (monthly_payment * count_periods))
    years = int(count_periods / 12)
    months = count_periods - (years * 12)
    if years == 0:
        print (f"You need {months} months to repay this credit!")
    elif months == 0:
        print(f"You need {years} years to repay this credit!")
    else:
        print(f"You need {years} years and {months} months to repay this credit!")
    print(f"Overpayment = {overpayment}")
        
def annuity_monthly_payment(credit_principal, number_of_periods, credit_interest):
    nominal_interes_rate = credit_interest
    annuity_payment = ceil(credit_principal * (((nominal_interes_rate * pow(1 + nominal_interes_rate, number_of_periods))) / (pow((1 + nominal_interes_rate), number_of_periods) - 1)))
    overpayment = abs(credit_principal - (annuity_payment * number_of_periods))
    print(f"Your annuity payment = {annuity_payment}!")
    print(f"Overpayment = {overpayment}")

def count_credit_principal(annuity_payment, number_of_periods, credit_interest):
    nominal_interes_rate = credit_interest
    credit_principal = ceil(annuity_payment / (((nominal_interes_rate * pow(1 + nominal_interes_rate, number_of_periods))) / (pow((1 + nominal_interes_rate), number_of_periods) - 1)))
    overpayment = abs(credit_principal - (annuity_payment * number_of_periods))
    print(f"Your loan principal = {credit_principal}!")
    print(f"Overpayment = {overpayment}")
    
def diff(principal, periods, interest):
    i = 1
    result = 0
    while i <= periods:
        D = ceil(principal / periods + interest * (principal - ((principal * (i - 1) / periods))))
        print(f"Month {i}: payment is {D}")
        result += D
        i += 1
    overpayment = abs(principal - result)
    print(f"\nOverpayment = {overpayment}")
parser = argparse.ArgumentParser()

parser.add_argument('--type', help="Type of the calculation")
parser.add_argument('--principal', help="The credit principal")
parser.add_argument('--periods', help="Number of periods")
parser.add_argument('--interest', help="Interest rate in %")
parser.add_argument('--payment', help="Amount of payment")

args=parser.parse_args()

if args.type == "diff":
    if len(sys.argv) == 5:
        if args.principal is None or args.periods is None or args.interest is None:
            print("Incorrect parameters.")
        else:
            principal = int(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)/1200
            diff(principal, periods, interest)
    else:
        print("Incorrect parameters.")
elif args.type == "annuity":
    if len(sys.argv) == 5:
        if args.principal is None:
            periods = int(args.periods)
            interest = float(args.interest)/1200
            payment = int(args.payment)
            count_credit_principal(payment, periods, interest)
        elif args.payment is None:
            periods = int(args.periods)
            interest = float(args.interest)/1200
            principal = int(args.principal)
            annuity_monthly_payment(principal, periods, interest)
        elif args.periods is None:
            interest = float(args.interest)/1200
            principal = int(args.principal)
            payment = int(args.payment)
            number_of_months(principal, payment, interest)
    else:
            print("Incorrect parameters.")


#mode(step)
