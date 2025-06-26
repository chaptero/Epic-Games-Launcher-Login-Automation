def read_accounts_from_file(file_path):
    accounts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                email, password = line.strip().split(',')
                accounts.append({'email': email, 'password': password})
    except FileNotFoundError:
        print("Account file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return accounts

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    return len(password) >= 6  # Example validation: password must be at least 6 characters long

def prompt_user_for_account_selection(accounts):
    print("Select an account to log in:")
    for index, account in enumerate(accounts):
        print(f"{index + 1}: {account['email']}")
    selection = input("Enter the number of the account you want to use: ")
    try:
        selected_index = int(selection) - 1
        if 0 <= selected_index < len(accounts):
            return accounts[selected_index]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None