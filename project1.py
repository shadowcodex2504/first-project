exp = {}

try:
    with open('exp.txt','r') as f:
        for line in f:
            category,amount = line.strip().split(',')
            amount = float(amount)
            if category in exp :
                exp[category].append(amount)
            else :
                exp[category] = [amount]
except:
    open('exp,txt','w').close()

def add_expenses(category,amount):
    if category in exp :
        exp[category].append(amount)
    else :
        exp[category] = [amount]
    
    # saving data to file
    with open('exp.txt','a') as file:
        file.write(f"{category},{amount}\n")

def show_summ():
    print("\nExpenses Summary:")
    try:
        with open('exp.txt','r') as file:
            lines = file.readlines()
            if not lines :
                print('You have ZERO Expenses')
                return

            exp_data = {}
            for line in lines :
                category,amount = line.strip().split(',')
                amount = float(amount)
                if category in exp_data:
                    exp_data[category].append(amount)
                else:
                    exp_data[category] = [amount]

            s = 0
            for cate,amts in exp_data.items():

                total = sum(amts)
                print(f'{cate} : ₹{amts}')
                s += total
            print(f'Total amount : ₹{s}')
    except Exception as e:
        print(f"Error : {e}")


            
while True:
    print("\n            1. Add Expense")
    print("            2. Show Summary")
    print("            3. Clear list")
    print("            4. Create a new Expense")
    print("            5. Exit")
    try:
        choice =int(input('Choose an Option:'))
    except:
        print("Please check your choice again")
        continue

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
    
    elif choice == 4:
        que = input('Are You Sure ,You to create a new file? \nThis will erase all the existing data. (Y/N) :').upper()
        if que == 'Y':
            exp.clear()
            with open('exp.txt','w') as f:
                f.write("")
            print("A new file is created")
        else:
            print('Operstion cancelled')

    elif choice ==5:
        print("Have a Nice Day")
        break
    else:
        print('Invalid Input!!!\nTry Again Please')

