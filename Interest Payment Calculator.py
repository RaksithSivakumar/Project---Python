def main():
    print("This a monthly payment loan calculator")

    principal = float(input("The loan amount: "))
    apr = float(input("The annual interest rate: "))
    year = float(input("Amount of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = year *12
    monthly_payment = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-amount_of_months))


    print("The monthly payment for this loan is : " + str(monthly_payment))

    main()
