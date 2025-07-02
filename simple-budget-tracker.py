import os

transactions = []

# Load existing transactions if file exists
if os.path.exists("transactions.txt"):
    with open("transactions.txt", "r") as file:
        for line in file:
            t_type, t_amount, t_description = line.strip().split(",", 2)
            transactions.append({
                'type': t_type,
                'amount': float(t_amount),
                'description': t_description
            })

while True:
    print('\n1. Add income')
    print('2. Add expense')
    print('3. Show balance')
    print('4. Show all transactions')
    print('5. Exit')

    option = input("Choose an option: ")

    if option == '1':
        print('Add income')
        amount = float(input('Insert amount: '))
        description = input('Enter income description: ')
        transaction = {
            'type': 'income',
            'amount': amount,
            'description': description
        }
        transactions.append(transaction)
        with open("transactions.txt", "a") as file:
            file.write(f"income,{amount},{description}\n")
        print('Income added successfully!')

    elif option == '2':
        print('Add expense')
        amount = float(input('Insert expense amount: '))
        description = input('Description of expense: ')
        transaction = {
            'type': 'expense',
            'amount': amount,
            'description': description
        }
        transactions.append(transaction)
        with open("transactions.txt", "a") as file:
            file.write(f"expense,{amount},{description}\n")
        print('Expense added successfully!')

    elif option == '3':
        print('Show balance')
        balance = 0
        for t in transactions:
            if t['type'] == 'income':
                balance += t['amount']
            else:
                balance -= t['amount']
        print(f'Current balance: £{balance:.2f}')

    elif option == '4':
        print('Show all transactions')
        if not transactions:
            print('No transactions yet.')
        else:
            for i, t in enumerate(transactions, start=1):
                print(f"{i}. {t['type'].capitalize()} - £{t['amount']:.2f} - {t['description']}")

    elif option == '5':
        print('Exit')
        break

    else:
        print('Invalid input. Please choose a valid option.')
