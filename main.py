MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter a amount that would you like to deposit $ ")
        
        if(amount.isdigit()):
            amount = int(amount)

            if(amount > 0):
                break

            else:
                print("Amount must be greater than 0")


        else:
            print("Please Enter a Number!! ")

    return amount


def get_number_of_line():
    while True:
        lines = input("How many line you want to Bet On(1,2,3)? ")

        if(lines.isdigit()):
            lines = int(lines)
            if(lines >= 1 and lines <= 3):
                break
                
            else:
                print("lines must between 1-3")

        else:
            print("please Enter a Number between 1-3!!")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if(amount.isdigit):
            amount = int(amount)
            if(amount >= MIN_BET and amount <= MAX_BET):
                break

            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
            
        else:
            print("Please Enter a Digit Only!!")

    return amount



balance = deposit()
lines = get_number_of_line()

while True:
    amount = get_bet()
    total_bet = amount * lines
    if(total_bet > balance):
        print(f"Do don't have enough balance to Bet!!..Your current balance is ${balance}")

    else:
        break

print(f"You are betting ${amount} on each {lines} lines. Total bet is equal to ${total_bet}")

    