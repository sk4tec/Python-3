money_owed = float(input("How much money do you owe in dollars?: ")) #50,000
annual_interest_rate = float(input("What is the annual interest rate (as a percent)?: ")) #3
payment = float(input("What is your monthly payment in dollars?: ")) #1,000
months = int(input("How many months have you been paying?: ")) # 24

monthly_interest_rate = annual_interest_rate / 100 / 12

for month in range(months):
    #calculate interest to pay per month
    interest = money_owed * monthly_interest_rate

    #add interest
    money_owed += interest

    if money_owed - payment < 0:
        print("You can pay off your loan early in month(s)", month + 1)
        print('Final payment:', money_owed)
        break

    # make payment
    money_owed -= payment
    print('Paid', payment, 'of which', interest, 'was interest.')
    print('Money still owed:', money_owed)