expenses = {}
def add_expenses(category,amount):
    if category in exp :
        exp[category].append(amount)
    else :
        exp[category] = [amount]

def show_summ():
    print("\nExpenses Summary:")
    for cate,amts in exp.items():
        total = sum(amts)
        print(f'{cate} : ₹{total}')


while True:
    print("\n1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")
    choice = input('Choose an Option:')

    if choice == 1:
        cat = input("Enter category (Like Food, Travel) :")
        amt = float(input('Enter Amount :₹'))
        add_expenses(cat,amt)
        print('Expense Added Successfully!')
    elif choice == 2:
        show_summ()
    elif choice == 3:
        print("Have a Nice Day")
        break
    else:
        print('Invalid Input!!!\nTry Again Please')


