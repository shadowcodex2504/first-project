exp = {}

def add_expenses(category,amount):
    if category in exp :
        exp[category].append(amount)
    else :
        exp[category] = [amount]

def show_summ():
    s = 0
    print("\nExpenses Summary:")
    if exp == {}:
        print("You have ZERO expenses")
    else:
        for cate,amts in exp.items():
            total = sum(amts)
            print(f'{cate} : ₹{total}')
            s += total
        print(f'Total Amount: ₹{s}')

            
while True:
    print("\n          1. Add Expense")
    print("            2. Show Summary")
    print("            3. Clear list")
    print("            4. Exit")
    try:
        choice =int(input('Choose an Option:'))
    except:
        print("Please check your choice again")

    if choice ==1:
        cat = input("Enter category (Like Food, Travel) :").upper()
        try:
            amt = float(input('Enter Amount :₹'))
        except:
            print('--Enter AMOUNT only--')
            continue
        add_expenses(cat,amt)
        print('Expense Added Successfully!')
        
    elif choice ==2:
        show_summ()

    elif choice == 3:
        exp.clear()
        print("Your Expenses List is CLEARED")

    elif choice ==4:
        print("Have a Nice Day")
        break
    else:
        print('Invalid Input!!!\nTry Again Please')

