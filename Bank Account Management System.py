import pickle
import os

credentials = {}
users_database = {}
Passbook = {}

def load_data():
    global credentials, users_database, Passbook
    if os.path.exists('bank_data.pkl'):
        with open('bank_data.pkl', 'rb') as f:
            data = pickle.load(f)
            credentials = data['credentials']
            users_database = data['users_database']
            Passbook = data['Passbook']

def save_data():
    with open('bank_data.pkl', 'wb') as f:
        data = {'credentials': credentials, 'users_database': users_database, 'Passbook': Passbook}
        pickle.dump(data, f)

# Load data at the start
load_data()

print("-" * 10, "Welcome to bank", "-" * 10)
print("\nHow can we help you today?")

while True:
    print("""1. Open a bank account?
2. View account details
3. Perform transactions (Cash Deposit/ Withdraw/ Transfer)
4. View transaction history
5. Exit """)

    try:
        Choice = int(input("Enter your choice between 1 to 5: "))
    except ValueError:
        print("Invalid input, please enter a number from 1 to 5")
        continue

    if Choice == 1:
        First_name = input("Enter first name: ")
        Last_name = input("Enter last name: ")
        Age = int(input("Enter your age: "))
        Phone_number = int(input("Enter your phone number: "))
        Pancard_number = input("Enter your pancard number: ")

        if Pancard_number in users_database.keys():
            print("Your account already exists. Try again")
            continue

        import random 
        account_number = "".join([str(random.randint(0, 9)) for _ in range(12)])

        account_type = input("What type of bank account do you want to open (current/savings)? ")
        Balance = int(input("How much amount do you wish to deposit? "))

        Username = First_name
        for i in range(2):
            a = random.randint(0, 9)
            Username = Username + str(a)

        Password = "".join([str(random.randint(0, 9)) for _ in range(4)])

        print("-" * 30)
        print("Your bank account is: ", account_type) 
        print("Your assigned username is: ", Username)
        print("Your assigned password is: ", Password)
        print("Your account number is: ", account_number)
        print("Your account balance is: ", Balance)
        print("Your pancard number is: ", Pancard_number)
        print("-" * 30)

        credentials[Username] = Password
        users_database[Pancard_number] = [First_name, Last_name, account_number, account_type, Balance]

    elif Choice == 2:
        un = input("Enter username: ") 
        Pw = input("Enter password: ") 
        Pc = input("Enter pancard number: ")

        if un in credentials.keys() and Pw == credentials[un] and Pc in users_database.keys(): 
            print("Your account details are: ") 
            print("Account holder name is: ", users_database[Pc][0], users_database[Pc][1]) 
            print("Account number is: ", users_database[Pc][2]) 
            print("Account type is: ", users_database[Pc][3]) 
            print("Account balance is: ", users_database[Pc][4]) 
        else: 
            print("This account does not exist. Try again.")

    elif Choice == 3:
        un = input("Enter username: ") 
        Pw = input("Enter password: ") 
        Pc = input("Enter pancard number: ")

        if un in credentials.keys() and Pw == credentials[un] and Pc in users_database.keys():
            print("""Press 1 to deposit
            Press 2 to withdraw
            Press 3 to transfer""")

            try:
                Transaction_Type = int(input("Enter transaction type (1/2/3): "))
            except ValueError:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue

            import datetime
            timestamp = datetime.datetime.now()

            if Transaction_Type == 1:
                transaction_amount = float(input("Enter amount: "))
                users_database[Pc][4] += transaction_amount
                print("Your current balance is: ", users_database[Pc][4])

            elif Transaction_Type == 2:
                transaction_amount = float(input("Enter withdraw amount: "))
                if transaction_amount > users_database[Pc][4]:
                    print("You cannot withdraw an excess amount")
                else:
                    users_database[Pc][4] -= transaction_amount
                    print("Remaining balance is: ", users_database[Pc][4])

            elif Transaction_Type == 3:
                receiver_account = input("Enter the receiver's pancard: ")
                transaction_amount = float(input("Enter the amount: "))
                if transaction_amount > users_database[Pc][4]:
                    print("You cannot transfer an excess amount")
                else:
                    users_database[Pc][4] -= transaction_amount
                    if receiver_account in users_database.keys():
                        users_database[receiver_account][4] += transaction_amount
                    print("Remaining balance is: ", users_database[Pc][4])

            if Pc in Passbook.keys():
                Passbook[Pc].append((timestamp, Transaction_Type, transaction_amount, users_database[Pc][4]))
            else:
                Passbook[Pc] = [(timestamp, Transaction_Type, transaction_amount, users_database[Pc][4])]

            print("Transaction recorded successfully.")

    elif Choice == 4:
        un = input("Enter username: ") 
        Pw = input("Enter password: ") 
        Pc = input("Enter pancard number: ")

        if un in credentials.keys() and Pw == credentials[un] and Pc in users_database.keys():
            print("     Timestamp       |   Transaction Type   |   Amount   |   Balance")
            for record in Passbook.get(Pc, []):
                print(record[0], record[1], record[2], record[3], sep=" | ")

    elif Choice == 5:
        save_data()
        break

    else:
        print("Invalid choice. Please select a valid option.")



        




